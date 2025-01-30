Digitales Mutterschiff für Sternenfahrer von Catan
Willkommen zu dieser inoffiziellen Erweiterung, die das legendäre Mutterschiff aus Sternenfahrer von Catan digital abbildet.
Gerade wenn die alten physischen Raumschiff-Modelle nicht mehr funktionieren oder beschädigt sind, ersetzt diese App das analoge Mutterschiff. Sie übernimmt das Würfeln (das Ziehen der Kugeln) sowie das Verwalten aller Ausbauten für jeden Spieler und jede Spielerin.

Funktionsübersicht
Digitales Mutterschiff: Kein langwieriges Schütteln der Kugeln mehr. Ein Klick auf "Wurf ausführen" genügt und die App zieht virtuelle Kugeln, errechnet die Grundgeschwindigkeit und zeigt an, ob eine Begegnung (schwarze Kugel) stattfindet.
Ausbauten verwalten: Jeder Spieler kann bequem Antriebe, Bordkanonen und Frachtmodule in der App erhöhen oder reduzieren.
Ruhmesringe & Freundschaftskarten: Die App zeigt den Fortschritt der Ruhmesringe (Medaillen) und ermöglicht das Verwalten von Freundschaftskarten (z. B. +2 Antrieb, +2 Kampfkraft, +1 Kombi).
Übersicht: Es gibt eine Ansicht, in der alle Spielenden mit ihren jeweiligen Ausbaustufen, letztem Wurf, Ruhmesringen etc. auf einen Blick angezeigt werden. Ideal für einen zentralen Bildschirm.
Mehrgeräte-Unterstützung: Jede*r kann das eigene Smartphone verwenden, um den persönlichen Spielstatus und Würfe zu verwalten. Eine Echtzeit-Kommunikation via WebSocket sorgt dafür, dass alle stets denselben aktuellen Stand sehen.
Projektstruktur
In diesem Repository befinden sich im Wesentlichen zwei Dateien:

server.py

Startet einen HTTP-Server (auf Port 8000), der die Datei index.html ausliefert.
Startet einen WebSocket-Server (auf Port 8765), der alle Spielzustandsänderungen an alle verbundenen Clients synchron überträgt.
Enthält die komplette Spiel-Logik (z. B. welche Kugeln gezogen werden, wie die Grundgeschwindigkeit berechnet wird, wie Ausbauten aktualisiert werden usw.).
Speichert den Spielzustand im Arbeitsspeicher.
index.html

Enthält das Frontend (HTML, CSS, JavaScript) mit Vue.js.
Stellt das UI für jeden Spieler (bzw. jedes Endgerät) bereit:
Spieler erstellen, auswählen oder löschen
Ausbauten / Ausrüstung anpassen
Aktuellen Würfelwurf / Kugelzug ausführen
Ruhmesringe und Freundschaftskarten pflegen
Anzeige aller Spielenden in einer Übersichtsseite
Voraussetzungen
Python 3.7 oder höher (getestet mit Python 3.9 und 3.10).
Das Python-Paket websockets zur Realisierung der WebSocket-Verbindungen.
Installiere das websockets-Paket beispielsweise so:

bash
Kopieren
Bearbeiten
pip install websockets
(oder im Kontext eines virtuellen Environments deiner Wahl).

Installation & Start
Repository klonen oder die Dateien server.py und index.html in ein Verzeichnis deiner Wahl kopieren.

Abhängigkeiten installieren (siehe oben).

bash
Kopieren
Bearbeiten
pip install websockets
Server starten:

bash
Kopieren
Bearbeiten
python server.py
Der Server startet dann zwei Dienste:

HTTP-Server: Port 8000
WebSocket-Server: Port 8765
Browser öffnen: Gehe im Browser (z. B. Chrome oder Firefox) auf http://localhost:8000. Dort wird dir die Startseite (index.html) angezeigt.

Mehrere Geräte verbinden:

Befinden sich alle Geräte (Smartphones, Tablets, weitere Laptops) im gleichen Netzwerk, kann jede*r Teilnehmende über http://IP-des-Rechners:8000 auf dieselbe Oberfläche zugreifen. Beispiel: http://192.168.0.42:8000 (IP des Servers einsetzen).
Alle UIs sind in Echtzeit via WebSocket synchronisiert. Eine Änderung (z. B. ein Wurf) wird unmittelbar auf allen geöffneten Seiten angezeigt.
Nutzung
Neuen Spieler erstellen (Startseite, sofern noch kein Spieler ausgewählt ist):

Namen eintragen, Farbe wählen, "Spieler erstellen" klicken.
In der Top-Bar (fixierte Leiste am oberen Bildschirmrand) erscheint eine Spieler-Badge mit dem Namen und der gewählten Farbe.
Spieler-Auswahl:

Über die Top-Bar kann man zwischen "Home" (Hauptmenü), "Übersicht" (Gesamtüberblick) und den vorhandenen Spielern wechseln.
Klickt man auf den Badge eines Spielers, öffnet sich dessen individuelles Mutterschiff-Dashboard.
Ausbauten verwalten:

Im Spieler-Dashboard können Antriebe, Bordkanonen und Frachtmodule (+/-) angepasst werden.
Alle Anpassungen werden automatisch an den Server gesendet und synchronisiert.
Wurf ausführen:

Per Klick auf "Wurf ausführen" werden digital Kugeln gezogen.
Das Ergebnis (Farben der Kugeln) sowie die Grundgeschwindigkeit wird angezeigt.
Sollte die schwarze Kugel auftauchen, findet eine Begegnung statt.
Ruhmesringe & Freundschaftskarten:

Die Anzahl der Ruhmesringe kann erhöht oder verringert werden (z. B. pro errungene Medaille).
Freundschaftskarten werden per Checkbox aktiviert/deaktiviert (z. B. +2 auf Antrieb, +2 auf Kampfkraft, usw.).
Die daraus entstehenden Boni fließen in die Gesamtgeschwindigkeit bzw. in die Kampfkraft ein.
Übersicht:

In der Top-Bar auf "Übersicht" klicken, um eine Grid-Ansicht aller Spielenden zu sehen.
Dort kann jeder Wert (Antrieb, Kanonen, Fracht, Medaillen) ebenfalls per Button angepasst und gewürfelt werden.
Perfekt für einen gemeinsamen Bildschirm oder Beamer.
Spiel zurücksetzen:

Im Spieler-Dashboard kann das ganze Spiel auf Null gesetzt werden (Button "Spiel zurücksetzen").
Daraufhin sind alle Spieler und Werte gelöscht.
Interne Abläufe
Echtzeit-Update:

server.py verwaltet den zentralen Spielzustand in einer Python-Variable.
Sobald ein Spieler-Update (z. B. Wurf) empfangen wird, speichert server.py das Ergebnis und broadcastet per WebSocket an alle Clients den neuen Zustand.
Die index.html-Oberfläche ist mit Vue.js realisiert und reagiert auf den aktualisierten Zustand, sodass alle Geräte stets dieselbe Ansicht haben.
Server-Architektur:

Ein einfacher HTTP-Server (Port 8000) liefert statische Dateien aus (insbesondere unsere index.html).
Parallel läuft ein WebSocket-Server (Port 8765), der eingehende Meldungen verarbeitet und allen Teilnehmenden den aktualisierten Spielzustand zusendet.
Kugeln:

Wir gehen davon aus, dass im Originalspiel (klassische Version) vier Farben im Beutel sind (gelb, rot, blau, schwarz – optional grün). Diese sind in server.py hinterlegt.
Beim Wurf wird per random.sample(...) genau zwei Kugeln gezogen.
Befindet sich schwarz darunter, wird die Grundgeschwindigkeit automatisch auf 3 gesetzt, ansonsten wird sie aus den Einzelwerten der Farben summiert.
Tipps zur Anpassung
Anpassung der Kugeln: In server.py kann man die Liste MARBLE_BAG verändern, falls man zusätzliche Farben oder unterschiedliche Häufigkeiten verwenden möchte.
GUI-Design: Alle Styles sind inline in index.html definiert (unter <style>). Dort kann man beliebig anpassen oder erweitern.
Bekannte Einschränkungen
Kein langfristiges Speichern: Die aktuelle Implementierung speichert den Spielstand nur im RAM des Servers. Ein Neustart von server.py setzt das Spiel daher zurück.
(Noch) keine Authentifizierung: Jede*r, der den Link zum Server kennt, kann Änderungen vornehmen. Für den Hausgebrauch ist das in der Regel ausreichend.
Beispielablauf
Server starten:
bash
Kopieren
Bearbeiten
python server.py
Browser aufrufen: http://localhost:8000
Im Home-Bildschirm neue Spieler anlegen (Name + Farbe).
Top-Bar nutzen, Spieler auswählen, Ausbauten und Ruhmesringe verwalten.
"Wurf ausführen" und die virtuellen Kugeln inklusive Grundgeschwindigkeit ablesen.
Mehrere Endgeräte verbinden, um das Spiel zu verteilen.
Lizenz und Dank
Dieses Projekt ist ein Fan-Projekt und steht in keiner offiziellen Verbindung mit Catan oder Kosmos.
Die Weitergabe und Nutzung erfolgt unter den Bedingungen der MIT License.

Viel Spaß beim erneuten Erkunden des Weltalls mit Sternenfahrer von Catan – diesmal mit einem digitalen Mutterschiff!

Kontakt / Feedback
Fragen und Anregungen gerne als GitHub-Issue oder via Pull Request einreichen.

Viel Erfolg und gutes Reisen durch die Galaxis!







Du:
kannst du mir das nochmal entsprechend aufgehübscht als markdown mit ein paar emojis ausgeben?

Thought about README mit Emojis für ein paar Sekunden
🚀 Digitales Mutterschiff für Sternenfahrer von Catan
Willkommen zu dieser inoffiziellen Erweiterung, die das legendäre Mutterschiff aus Sternenfahrer von Catan digital abbildet.
Gerade wenn die alten physischen Raumschiff-Modelle den Geist aufgegeben haben oder beschädigt sind, ersetzt diese App das analoge Mutterschiff. Sie übernimmt das Würfeln (Kugel-Ziehen) sowie das Verwalten aller Ausbauten für jeden Spieler und jede Spielerin.

Hinweis: Das Projekt steht in keiner offiziellen Verbindung mit Catan oder Kosmos und ist lediglich ein Fan-Projekt.

🪐 Funktionsübersicht
Digitales Mutterschiff:
Per Klick auf „Wurf ausführen“ werden virtuelle Kugeln gezogen, die Grundgeschwindigkeit wird berechnet und eine Begegnung (schwarze Kugel) angezeigt.

Ausbauten verwalten:
Jeder kann Antriebe, Bordkanonen und Frachtmodule bequem in der App einstellen – kein Fummeln am echten Plastikschiff mehr.

Ruhmesringe & Freundschaftskarten:
Einfaches Erfassen der Ruhmesringe (Medaillen) sowie Verwaltung von Freundschaftskarten (+2 Antrieb, +2 Kampfkraft oder +1 Kombi).

Übersicht mit allen Spielenden:
Perfekt für einen zentralen Bildschirm: Anzeige aller Spieler mit jeweiligen Ausbauten, Würfen und Ruhmesringen in einer praktischen Grid-Ansicht.

Mehrgeräte-Unterstützung:
Jeder kann von seinem Smartphone, Tablet oder Laptop das eigene Schiff steuern. Durch WebSocket-Synchronisation sind alle Daten sofort aktuell.

📁 Projektstruktur
In diesem Repository findest du im Wesentlichen zwei Dateien:

server.py

Startet einen HTTP-Server (Port 8000), der die index.html ausliefert
Startet einen WebSocket-Server (Port 8765), über den alle Clients synchronisiert werden
Beinhaltet die Spiel-Logik (Kugel-Ziehen, Ausbauten aktualisieren etc.)
Speichert den aktuellen Spielzustand im Arbeitsspeicher
index.html

Enthält das Frontend mit HTML, CSS und Vue.js (per CDN)
Stellt das UI für jeden Spieler zur Verfügung:
Spieler erstellen, auswählen oder löschen
Ausbauten setzen
Wurf ausführen
Ruhmesringe und Freundschaftskarten pflegen
Übersicht aller Spielenden
⚙️ Voraussetzungen
Python 3.7 oder höher (getestet unter Python 3.9/3.10)
Das Python-Paket websockets zur Realisierung der WebSocket-Kommunikation:
bash
Kopieren
Bearbeiten
pip install websockets
(Ggf. in einem virtuellen Environment deiner Wahl.)

🚀 Installation & Start
Repository klonen oder die Dateien server.py und index.html in ein beliebiges Verzeichnis kopieren.

Abhängigkeiten installieren (mindestens websockets):

bash
Kopieren
Bearbeiten
pip install websockets
Server starten:

bash
Kopieren
Bearbeiten
python server.py
Der Server wird auf

Port 8000 (HTTP) und
Port 8765 (WebSocket)
laufen.
Browser öffnen:
Gehe auf http://localhost:8000. Dort findest du die Startseite mit allen Funktionen.

Mehrere Geräte verbinden:

Auf anderen Endgeräten im gleichen (WLAN-)Netz einfach http://IP-des-Servers:8000 im Browser aufrufen.
Alle UIs sind in Echtzeit miteinander synchronisiert.
💡 Nutzung
Spieler erstellen
Auf der Startseite Namen und Farbe eingeben
„Spieler erstellen“ klicken
In der Top-Bar erscheint eine Badge mit Name & Farbe
Spieler auswählen
In der Top-Bar auf den Badge des Spielers klicken, um dessen individuelle Schiffsübersicht zu sehen
Ausbauten einstellen
Innerhalb des gewählten Spielers:
Antriebe, Bordkanonen und Frachtmodule über Plus/Minus-Buttons anpassen
Würfeln
Per Klick auf „Wurf ausführen“ zieht der Server 2 Kugeln aus dem virtuellen Beutel
Angezeigt werden:
Farben der Kugeln (z.B. Rot, Blau oder Schwarz)
Grundgeschwindigkeit
Falls eine schwarze Kugel erscheint, gibt es eine Begegnung!
Ruhmesringe & Freundschaft
Ruhmesringe (Medaillen) können hoch-/runtergezählt werden
Freundschaftskarten werden per Checkbox aktiviert/deaktiviert
Übersicht
Über die Top-Bar „Übersicht“ anzeigen lassen
Zeigt alle Spieler mit ihren Ausbauten, Ruhmesringen und letztem Wurf
Ideal für einen geteilten Bildschirm oder Beamer
Spiel zurücksetzen
Im Einzelspieler-Dashboard kannst du das gesamte Spiel auf Null zurücksetzen
🔧 Hinter den Kulissen
Echtzeit-Update:
server.py speichert alles in GAME_STATE. Jede Aktion (Ausbau ändern, Würfeln etc.) wird vom Client an den Server gesendet. Dieser aktualisiert den Zustand und verteilt ihn per Broadcast via WebSocket an alle verbundenen Clients.

Kugel-Zieh-Logik:

Standardmäßig wird aus ["gelb", "gelb", "rot", "blau", "schwarz"] per random.sample gezogen
schwarze Kugel ⇒ Grundgeschwindigkeit = 3, ansonsten wird sie aus den Farbwerten summiert
Datei-Serving:

Ein einfacher HTTP-Server (Port 8000) liefert statische Dateien (vor allem index.html) aus
Keine persistente Speicherung:

Nach einem Neustart von server.py sind alle Daten weg
Für den Hausgebrauch reicht das aber in der Regel
🔋 Tipps zur Anpassung
Kugeln: In server.py kann man den Beutel MARBLE_BAG beliebig anpassen oder mehr Kugeln hinzufügen.
Maximale Ausbauten: Standardmäßig sind 6 Antriebe / Kanonen und 5 Frachtmodule als Obergrenze hinterlegt. Bei Bedarf ändern.
GUI-Styling: Sämtliche CSS-Regeln sind in index.html enthalten. Dort kann man Farben, Schriftarten usw. anpassen.
⚠️ Bekannte Einschränkungen
Nur RAM-Speicherung: Kein automatisches Speichern des Zustands auf Festplatte.
Keine Zugriffsbeschränkung: Wer den Link kennt, kann mitspielen oder manipulieren.
Beispiel: Schneller Ablauf
Server starten
bash
Kopieren
Bearbeiten
python server.py
http://localhost:8000 im Browser öffnen
Spieler anlegen (Name + Farbe)
Spieler aus Top-Bar auswählen, Ausbauten setzen
Wurf ausführen – das System zeigt die Kugeln und berechnet die Grundgeschwindigkeit
Mehrere Geräte verbinden (Mobil, Tablet, etc.)
Überblick in der „Übersicht“-Seite genießen
🌟 Lizenz & Dank
Lizenz: MIT License
Danksagung:
Allen Sternenfahrer-Fans, die das Originalspiel lieben!
Und vielen Dank an die Vue.js-Community für die coole Framework-Basis.
Bei Fragen, Feedback oder Verbesserungsvorschlägen freuen wir uns über Issues oder Pull Requests.

Viel Erfolg und gutes Fliegen in der Galaxis! ✨
