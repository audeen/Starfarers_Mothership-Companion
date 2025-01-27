# Starfarers_Mothership-Companion
Digitales Mutterschiff-Demo

Dies ist ein Minimalbeispiel für ein digitales „Mutterschiff“ im Sternenfahrer von Catan-Stil, inklusive:

    HTTP-Server (liefert die statische index.html),
    WebSocket-Server (ermöglicht Echtzeit-Updates zwischen Server und Browsern),
    Demo-Frontend auf Basis von Vue.js (Version 3).

Das Projekt dient als Beispiel, wie man ein kleines Web-UI erstellen kann, um die Mechanik der Farb-Kugeln (Marbles) zu simulieren, die normalerweise in den physischen Sternenfahrer-Mutterschiffen enthalten sind.
Features

    HTTP-Server
    - Läuft standardmäßig auf Port 8000.
    - Liefert die Datei index.html (und ggf. weitere statische Assets) aus.

    WebSocket-Server
    - Läuft standardmäßig auf Port 8765.
    - Alle verbundenen Browser erhalten fortlaufend den gemeinsamen Spielzustand (GAME_STATE).
    - Änderungen (z. B. bei einem Wurf) werden an alle Clients verteilt.

    Vue-Frontend
    - Zeigt die Spieler, Ausbauten, Freundschaftskarten und Kugeln (Marbles) an.
    - Ermöglicht das Erstellen und Löschen von Spielern sowie das Auslösen eines Würfels (Ziehen von Kugeln).
    - Die Kugeln werden überall (Top-Bar, Overlay, Zusammenfassung) mit passenden CSS-Klassen gerendert.

Installation & Start

    Repository klonen oder alle Dateien in ein eigenes Verzeichnis kopieren.

    Abhängigkeit: Du benötigst Python 3 (z. B. 3.10 oder 3.11).

    Eventuell: pip install websockets (wenn noch nicht vorhanden).

    Starten:

python server.py

Anschließend siehst du Meldungen wie:

    HTTP-Server läuft auf http://localhost:8000
    WebSocket-Server läuft auf ws://localhost:8765

    Browser aufrufen: http://localhost:8000/

Ordnerstruktur

    server.py
    Enthält den Python-Code für HTTP- und WebSocket-Server. Verarbeitet die eingehenden Nachrichten (JSON) und speichert alles in GAME_STATE.
    index.html
    Das Frontend mit Vue 3. Baut eine WebSocket-Verbindung auf (ws://localhost:8765) und zeigt den Spielzustand interaktiv an (Ausbauten, Ruhmesringe, Wurf etc.).
    (Weitere Dateien)
    Eventuell zusätzliche .css, .js oder Assets. Hier im Minimalbeispiel ist alles in der index.html eingebunden.

Besonderheiten

    Kugeln (Marbles) werden im Server via random.sample(...) aus einer kleinen Liste gezogen (z. B. ["rot","blau","gelb","schwarz","gruen"]).
    Geschwindigkeitsberechnung (Grundgeschwindigkeit = 3, falls Schwarz dabei ist, sonst Summe der Farbwerte) ist in der Funktion compute_base_speed(kugeln) hinterlegt.
    Front-End nutzt normalizeMarbles(...), damit z. B. "Blau" → "blau" einheitlich zu einer gültigen CSS-Klasse gemappt wird. Dadurch tauchen keine || statt Kugeln auf.

Nutzung & Anpassungen

    Du kannst problemlos weitere Eigenschaften an den Spieler hängen (z. B. kampfkraft oder vorratskarten).
    Falls du Ports ändern möchtest, passe die entsprechenden Stellen in server.py an:

    port=8000        # HTTP-Port
    ws_port=8765     # WebSocket-Port

    In MARBLE_BAG (server.py) kannst du die Kugeln (und deren Häufigkeiten) ändern.
    In MARBLE_VALUES kannst du die Zahlenwerte für jede Farbe anpassen.

Bekannte Probleme / FAQ

    „EOFError: stream ends after 0 bytes…“
    – Typischerweise bedeutet es, dass ein Client (oder Browser-Plugin) eine HTTP-Anfrage an den WS-Port 8765 stellt (oder die Verbindung zu früh schließt). Meist ungefährlich, kann ignoriert werden.

    „WS nicht offen.“
    – Bedeutet, dass der Browser noch keine WebSocket-Verbindung aufbauen konnte oder diese bereits geschlossen wurde (z. B. beim Refresh). Warte kurz oder reconnecte.

    Kugeln werden nicht angezeigt, sondern ||:
    – Hier sollte das normalizeMarbles in index.html aushelfen. Prüfe in der Browser-Konsole, welche Werte wirklich im Array ankommen.

Lizenz

    Dieses Projekt hat keine offizielle Lizenz. Du kannst es frei anpassen und nutzen.
    Die Begriffe „Sternenfahrer“, „Catan“ usw. gehören dem jeweiligen Rechteinhaber. Dies hier ist nur ein Fan-Projekt / Demo.

Kontakt

    Bei Fragen: issue auf GitHub anlegen oder E-Mail an [Deine E-Mail-Adresse].
