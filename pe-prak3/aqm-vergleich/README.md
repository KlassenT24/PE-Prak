# AQM Vergleich Projekt

Dieses Projekt implementiert eine Active Queue Management (AQM) Methode, speziell die Random Early Detection (RED) Methode, um die Leistung von Netzwerkwarteschlangen zu verbessern. Es vergleicht die Latenz, den Paketverlust und den Durchsatz zwischen einer Standard-Queue und einer AQM-gestützten Queue.

## Projektstruktur

- `src/main.py`: Einstiegspunkt der Anwendung, der die Queue initialisiert und Experimente durchführt.
- `src/queue/base_queue.py`: Definiert die Basisklasse `BaseQueue` mit grundlegenden Methoden für eine Queue.
- `src/queue/red_queue.py`: Implementiert die `REDQueue`, die von `BaseQueue` erbt und die AQM-Logik enthält.
- `src/experiments/run_experiments.py`: Führt Experimente durch, um die Leistung der Standard- und RED-Queue zu messen.
- `src/analysis/evaluate_results.py`: Analysiert die Ergebnisse der Experimente und berechnet Durchschnittswerte.
- `src/utils/helpers.py`: Enthält Hilfsfunktionen für verschiedene Berechnungen und Datenoperationen.
- `requirements.txt`: Listet die Abhängigkeiten des Projekts auf.
- `results/summary`: Verzeichnis zur Speicherung der Experimentergebnisse.

## Installation

Um das Projekt auszuführen, stellen Sie sicher, dass Sie Python 3.x installiert haben. Installieren Sie die erforderlichen Abhängigkeiten mit:

```
pip install -r requirements.txt
```

## Nutzung

Führen Sie das Hauptskript aus, um die Experimente zu starten:

```
python src/main.py
```

Die Ergebnisse der Experimente werden im Verzeichnis `results/summary` gespeichert.