# 🚀 Digitales Mutterschiff für _Sternenfahrer von Catan_

Willkommen zu dieser inoffiziellen Erweiterung, die das legendäre Mutterschiff aus **Sternenfahrer von Catan** digital abbildet.  
Gerade wenn die alten physischen Raumschiff-Modelle den Geist aufgegeben haben oder beschädigt sind, ersetzt diese App das analoge Mutterschiff. Sie übernimmt das **Würfeln** (Kugel-Ziehen) sowie das **Verwalten aller Ausbauten** für jeden Spieler und jede Spielerin.  

> **Hinweis:** Das Projekt steht in keiner offiziellen Verbindung mit Catan oder Kosmos und ist lediglich ein Fan-Projekt.

---

## 🪐 Funktionsübersicht

- **Digitales Mutterschiff**:  
  Per Klick auf "Wurf ausführen" werden virtuelle Kugeln gezogen, die **Grundgeschwindigkeit** wird berechnet und eine **Begegnung** (schwarze Kugel) angezeigt.

- **Ausbauten verwalten**:  
  Jeder kann **Antriebe**, **Bordkanonen** und **Frachtmodule** bequem in der App einstellen – kein Fummeln am echten Plastikschiff mehr.

- **Ruhmesringe & Freundschaftskarten**:  
  Einfaches Erfassen der Ruhmesringe (Medaillen) sowie Verwaltung von Freundschaftskarten (+2 Antrieb, +2 Kampfkraft oder +1 Kombi).

- **Übersicht mit allen Spielenden**:  
  Perfekt für einen **zentralen Bildschirm**: Anzeige aller Spieler mit jeweiligen Ausbauten, Würfen und Ruhmesringen in einer praktischen Grid-Ansicht.

- **Mehrgeräte-Unterstützung**:  
  Jeder kann von seinem **Smartphone, Tablet oder Laptop** das eigene Schiff steuern. Durch **WebSocket**-Synchronisation sind alle Daten sofort aktuell.

---

## 📁 Projektstruktur

In diesem Repository findest du im Wesentlichen **zwei Dateien**:

1. **`server.py`**  
   - Startet einen **HTTP-Server** (Port `8000`), der die `index.html` ausliefert  
   - Startet einen **WebSocket-Server** (Port `8765`), über den alle Clients synchronisiert werden  
   - Beinhaltet die Spiel-Logik (Kugel-Ziehen, Ausbauten aktualisieren etc.)  
   - Speichert den aktuellen Spielzustand im Arbeitsspeicher

2. **`index.html`**  
   - Enthält das **Frontend** mit HTML, CSS und [Vue.js](https://vuejs.org/) (per CDN)  
   - Stellt das UI für jeden Spieler zur Verfügung:  
     - Spieler erstellen, auswählen oder löschen  
     - Ausbauten setzen  
     - Wurf ausführen  
     - Ruhmesringe und Freundschaftskarten pflegen  
     - Übersicht aller Spielenden  

---

## ⚙️ Voraussetzungen

- **Python 3.7 oder höher** (getestet unter Python 3.9/3.10)  
- Das Python-Paket **`websockets`** zur Realisierung der WebSocket-Kommunikation:

```bash
pip install websockets
```

> (Ggf. in einem virtuellen Environment deiner Wahl.)

---

## 🚀 Installation & Start

1. **Repository klonen** oder die Dateien `server.py` und `index.html` in ein beliebiges Verzeichnis kopieren.

2. **Abhängigkeiten installieren** (mindestens `websockets`):

   ```bash
   pip install websockets
   ```

3. **Server starten**:

   ```bash
   python server.py
   ```
   
   Der Server wird auf  
   - **Port 8000** (HTTP) und  
   - **Port 8765** (WebSocket)  
   laufen.

4. **Browser öffnen**:  
   Gehe auf [http://localhost:8000](http://localhost:8000). Dort findest du die Startseite mit allen Funktionen.

5. **Mehrere Geräte verbinden**:  
   - Auf anderen Endgeräten im gleichen (WLAN-)Netz einfach `http://IP-des-Servers:8000` im Browser aufrufen.  
   - Alle UIs sind in Echtzeit miteinander synchronisiert.

---

## 💡 Nutzung

### Spieler erstellen
- Auf der Startseite **Namen** und **Farbe** eingeben
- **„Spieler erstellen“** klicken
- In der **Top-Bar** erscheint eine Badge mit Name & Farbe

### Spieler auswählen
- In der **Top-Bar** auf den Badge des Spielers klicken, um dessen **individuelle Schiffsübersicht** zu sehen

### Ausbauten einstellen
- Innerhalb des gewählten Spielers:  
  **Antriebe**, **Bordkanonen** und **Frachtmodule** über Plus/Minus-Buttons anpassen

### Würfeln
- Per Klick auf **„Wurf ausführen“** zieht der Server **2 Kugeln** aus dem virtuellen Beutel
- Angezeigt werden:  
  - **Farben** der Kugeln (z.B. Rot, Blau oder Schwarz)  
  - **Grundgeschwindigkeit**  
  - Falls eine **schwarze Kugel** erscheint, gibt es eine Begegnung!

### Ruhmesringe & Freundschaft
- Ruhmesringe (Medaillen) können hoch-/runtergezählt werden
- Freundschaftskarten werden per **Checkbox** aktiviert/deaktiviert

### Übersicht
- Über die Top-Bar **„Übersicht“** anzeigen lassen
- Zeigt alle Spieler mit ihren Ausbauten, Ruhmesringen und letztem Wurf
- Ideal für einen **geteilten Bildschirm** oder **Beamer**

### Spiel zurücksetzen
- Im Einzelspieler-Dashboard kannst du das gesamte Spiel auf **Null** zurücksetzen

---

## 🔧 Hinter den Kulissen

- **Echtzeit-Update**:  
  `server.py` speichert alles in `GAME_STATE`. Jede Aktion (Ausbau ändern, Würfeln etc.) wird vom Client an den Server gesendet. Dieser aktualisiert den Zustand und verteilt ihn per **Broadcast** via WebSocket an **alle** verbundenen Clients.

- **Kugel-Zieh-Logik**:
  - Standardmäßig wird aus `["gelb", "gelb", "rot", "blau", "schwarz"]` per `random.sample` gezogen
  - **schwarze Kugel** ⇒ Grundgeschwindigkeit = 3, ansonsten wird sie aus den Farbwerten summiert

- **Datei-Serving**:
  - Ein einfacher HTTP-Server (Port 8000) liefert statische Dateien (vor allem `index.html`) aus

- **Keine persistente Speicherung**:
  - Nach einem Neustart von `server.py` sind alle Daten weg
  - Für den Hausgebrauch reicht das aber in der Regel

---

## Beispiel: Schneller Ablauf

1. **Server starten**  
   ```bash
   python server.py
   ```
2. **[http://localhost:8000](http://localhost:8000)** im Browser öffnen  
3. **Spieler anlegen** (Name + Farbe)  
4. **Spieler aus Top-Bar auswählen**, Ausbauten setzen  
5. **Wurf ausführen** – das System zeigt die Kugeln und berechnet die Grundgeschwindigkeit  
6. **Mehrere Geräte** verbinden (Mobil, Tablet, etc.)  
7. **Überblick** in der „Übersicht“-Seite genießen

---

Viel Erfolg und **gutes Fliegen** in der Galaxis! ✨

