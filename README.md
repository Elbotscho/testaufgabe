# Testaufgabe

Diese Web-Anwendung zeigt Versicherungsdaten an. Sie besteht aus einem Angular-Frontend, einem FastAPI-Backend und verwendet eine SQLite-Datenbank.

## Inhaltsverzeichnis
- [Vorwort](#vorwort)
- [Beschreibung](#beschreibung)
- [Installation](#installation)

## Vorwort

In dem Repository sind zwei Versionen der Anwendung enthalten:

1. Docker-Version: Diese Version nutzt ein Docker-System zur Containerisierung der Anwendung.
2. Nicht-Docker-Version: Falls die Docker-Version nicht einwandfrei funktioniert, stelle ich zusätzlich eine Version bereit, die auch ohne Docker läuft. So kann die bearbeitete Aufgabe dennoch begutachtet werden.

## Beschreibung 

Auf der Webseite finden Sie eine Navigationsleiste, die Links zu den drei verschiedenen Tabellenansichten enthält. Jeder Link führt zu einer detaillierten Ansicht, die die entsprechenden Datenbankeinträge in einer Tabelle anzeigt.

Im oberen rechten Bereich der Ansicht befindet sich ein Download-Button, mit dem Sie die Tabelleninhalte bequem als CSV-Datei herunterladen können.

## Installation

### Mit Docker

1. Öffne ein neues Terminal

2. Klone das Repository:

   git clone https://github.com/dein-benutzername/dein-repository.git

3. Navigiere in das Verzeichnis **Testaufgabe**: 

   cd Testaufgabe

4. Starte den Docker-Container:

   docker-compose up --build

Nachdem der Container gestartet ist kann die Seite http://localhost:4200 besucht werden.

### Ohne Docker

#### Backend (FastAPI)

1. Öffne ein neues Terminal

2. Klone das Repository:

   git clone https://github.com/dein-benutzername/dein-repository.git
   
3. Navigiere in das Backend-Verzeichnis der **Testaufgabe_ohne_docker**:

   cd Testaufgabe_ohne_docker/backend

4. Erstelle und aktiviere eine virtuelle Umgebung:

   Entweder mit python:
   
   	python -m venv venv
   	
   oder mit virtualenv:
   
   	pip install virtualenv
   
   	virtualenv venv
  
5. Aktiviere die virtuelle Umgebung:
   
   Windows:
   
   	venv\Scripts\activate
   
   Unix:
   
   	source venv/bin/activate
   	
6. Installiere die Abhängigkeiten:
   
   pip install -r requirements.txt
   
7. Führe die FastAPI-Anwendung aus:
   
   uvicorn main:app --reload
   
#### Frontend (Angular)

1. Öffne ein neues Terminal

2. Navigiere in das Frontend-Verzeichnis:
  
   cd Testaufgabe_ohne_docker/frontend
   
3. Installiere die Abhängigkeiten:
  
   npm install -g @angular/cli
   
4. Starte die Angular-Anwendung:
  
   ng serve

#### Datenbank (SQLite)

Die Datenbank ist bereits erstellt und befüllt.

#### Verwendung

1. Starte zunächst das Backend, indem du die FastAPI-Anwendung ausführst.
2. Starte dann das Frontend, indem du den Angular-Entwicklungsserver startest.
3. Öffne einen Webbrowser und gehe zu http://localhost:4200, um die Anwendung zu sehen.
