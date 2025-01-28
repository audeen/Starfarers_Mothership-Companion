#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PRODUKTIONSSERVER-SKRIPT:
 - Stellt einen HTTP-Server (Port 8000) bereit, der index.html und statische Dateien ausliefert.
 - Stellt einen WebSocket-Server (Port 8765) für die Echtzeitkommunikation bereit.

Die Spielmechanik ermöglicht das Ziehen und Auswerten von Kugeln verschiedener Farben
sowie das Verwalten von Spielern und deren Ausbauten.
"""

import http.server
import socketserver
import threading
import asyncio
import websockets
import json
import os
import random

# -------------------------------------------------------------------
# SPIELZUSTAND
# -------------------------------------------------------------------
GAME_STATE = {
    "players": {}
}
NEXT_PLAYER_ID = 1
CONNECTED_CLIENTS = set()

# Mögliche Kugeln (Beutel)
MARBLE_BAG = ["gelb","gelb","rot","blau","schwarz"]
# Werte der einzelnen Farben zur Berechnung der Geschwindigkeit
MARBLE_VALUES = {
    "schwarz": 0,
    "blau": 1,
    "gelb": 2,
    "rot": 3,
    "gruen": 1  # Hier exemplarisch für "gruen"
}

def reset_game_state():
    """
    Setzt das globale Spiel zurück.
    """
    global GAME_STATE, NEXT_PLAYER_ID
    NEXT_PLAYER_ID = 1
    GAME_STATE = {"players":{}}

def do_wurf():
    """
    Zieht per Zufall 2 Kugeln (ohne Zurücklegen) aus MARBLE_BAG.
    random.sample stellt sicher, dass nie derselbe Index zweimal gewählt wird.
    """
    return random.sample(MARBLE_BAG, 2)

def compute_base_speed(kugeln):
    """
    Berechnet die Grundgeschwindigkeit des Wurfs:
    - Falls "schwarz" dabei ist => 3
    - Sonst Summe der Einzelwerte (laut MARBLE_VALUES).
    """
    if "schwarz" in kugeln:
        return 3
    else:
        return sum(MARBLE_VALUES.get(k, 0) for k in kugeln)

async def broadcast_game_state():
    """
    Schickt allen verbundenen WebSocket-Clients den aktuellen GAME_STATE.
    """
    msg = {
        "type": "GAME_STATE",
        "payload": GAME_STATE
    }
    encoded = json.dumps(msg)
    for ws in CONNECTED_CLIENTS:
        await ws.send(encoded)

async def handle_message(msg):
    """
    Verarbeitet eine eingehende JSON-Message vom Client:
      {"action": "XYZ", "data": {...}}
    """
    global NEXT_PLAYER_ID
    action = msg.get("action")
    data   = msg.get("data", {})

    if action == "createPlayer":
        # Neuen Player anlegen
        pid = f"p{NEXT_PLAYER_ID}"
        NEXT_PLAYER_ID += 1
        name = data.get("name", "Unknown")
        col  = data.get("color", "gray")

        GAME_STATE["players"][pid] = {
            "name": name,
            "color": col,
            "antriebe": 0,
            "bordkanonen": 0,
            "frachtmodule": 0,
            "ruhmesringe": 1,
            "letzter_wurf": None,
            "friendship": {
                "kampf_plus2": False,
                "antrieb_plus2": False,
                "combo_plus1":  False
            }
        }

    elif action == "deletePlayer":
        # Player löschen
        pid = data.get("playerId")
        if pid in GAME_STATE["players"]:
            del GAME_STATE["players"][pid]

    elif action == "resetGame":
        # Kompletter Reset
        reset_game_state()

    elif action == "doWurf":
        # Neuer Wurf für einen Spieler
        pid = data.get("playerId")
        if pid in GAME_STATE["players"]:
            drawn = do_wurf()  # z.B. ["rot","schwarz"]
            base  = compute_base_speed(drawn)
            print(f"[SERVER] doWurf für {pid} => kugeln={drawn}, grund={base}")
            GAME_STATE["players"][pid]["letzter_wurf"] = {
                "kugeln": drawn,
                "grundgeschwindigkeit": base
            }

    elif action == "updateAusbau":
        # Antriebe/Bordkanonen/Frachtmodule anpassen
        pid = data.get("playerId")
        if pid in GAME_STATE["players"]:
            p = GAME_STATE["players"][pid]
            a = max(0, min(6, data.get("antriebe", 0)))
            b = max(0, min(6, data.get("bordkanonen", 0)))
            f = max(0, min(5, data.get("frachtmodule", 0)))
            p["antriebe"] = a
            p["bordkanonen"] = b
            p["frachtmodule"] = f

    elif action == "updateMedaillen":
        # Ruhmesringe erhöhen / verringern
        pid = data.get("playerId")
        d   = data.get("delta", 0)
        if pid in GAME_STATE["players"]:
            p = GAME_STATE["players"][pid]
            newv = p["ruhmesringe"] + d
            if newv < 0:
                newv = 0
            p["ruhmesringe"] = newv

    elif action == "toggleFriendship":
        # Freundschaftskarten umschalten (True/False)
        pid = data.get("playerId")
        t   = data.get("type")
        if pid in GAME_STATE["players"]:
            fr = GAME_STATE["players"][pid]["friendship"]
            if t in fr:
                fr[t] = not fr[t]

    # Nach jeder Änderung den State an alle verteilen
    await broadcast_game_state()

async def websocket_handler(ws):
    """
    Jede neue WebSocket-Verbindung wird hier behandelt.
    """
    CONNECTED_CLIENTS.add(ws)
    try:
        # Sende beim Connect den aktuellen Zustand
        await broadcast_game_state()

        async for raw in ws:
            try:
                m = json.loads(raw)
                await handle_message(m)
            except json.JSONDecodeError:
                print("[SERVER] JSON-Fehler:", raw)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        CONNECTED_CLIENTS.remove(ws)

# HTTP-Server: dient nur dazu, index.html + statische Ressourcen auszuliefern
class MyHttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Leite / auf /index.html um
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

def start_http_server():
    # Statisches Verzeichnis ist das aktuelle Skriptverzeichnis
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = 8000
    print(f"HTTP-Server läuft auf http://localhost:{port}")
    with socketserver.TCPServer(("", port), MyHttpHandler) as srv:
        srv.serve_forever()

async def start_ws():
    wport = 8765
    print(f"WebSocket-Server läuft auf ws://localhost:{wport}")
    async with websockets.serve(websocket_handler, "", wport):
        await asyncio.Future()  # läuft für immer

def main():
    # HTTP-Server in Thread starten
    t = threading.Thread(target=start_http_server, daemon=True)
    t.start()
    # Eventloop für WebSocket-Server
    asyncio.run(start_ws())

if __name__ == "__main__":
    main()
