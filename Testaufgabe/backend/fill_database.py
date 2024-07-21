from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json

from .database import Versichertendaten, Versicherungsvertrag, Schadensfall, engine

Session = sessionmaker(bind=engine)
session = Session()

# Funktion zum Einlesen der JSON-Dateien
def load_data_from_json(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
    return data

# Lade die Daten aus den JSON-Dateien
versicherte_data = load_data_from_json('testdaten/versicherte_daten.json')
vertraege_data = load_data_from_json('testdaten/vertraege_daten.json')
schadensfaelle_data = load_data_from_json('testdaten/schadensfaelle_daten.json')

# Füge die Daten in die Datenbank ein
for versichert_data in versicherte_data:
    versichert = Versichertendaten(
        versichertennummer=versichert_data['versichertennummer'],
        name=versichert_data['name'],
        geburtsdatum=datetime.strptime(versichert_data['geburtsdatum'], '%Y-%m-%d').date(),
        adresse=versichert_data['adresse']
    )
    session.add(versichert)

for vertrag_data in vertraege_data:
    vertrag = Versicherungsvertrag(
        vertragsnummer=vertrag_data['vertragsnummer'],
        versichertennummer=vertrag_data['versichertennummer'],
        vertragsbeginn=datetime.strptime(vertrag_data['vertragsbeginn'], '%Y-%m-%d').date(),
        vertragsende=datetime.strptime(vertrag_data['vertragsende'], '%Y-%m-%d').date() if vertrag_data['vertragsende'] else None,
        vertragsstatus=vertrag_data['vertragsstatus']
    )
    session.add(vertrag)

for schaden_data in schadensfaelle_data:
    schaden = Schadensfall(
        schadensnummer=schaden_data['schadensnummer'],
        vertragsnummer=schaden_data['vertragsnummer'],
        datum=datetime.strptime(schaden_data['datum'], '%Y-%m-%d').date(),
        schadenstyp=schaden_data['schadenstyp'],
        schadenhoehe=schaden_data['schadenhoehe']
    )
    session.add(schaden)

# Datenbankänderungen bestätigen
session.commit()
session.close()

print("Daten aus den JSON-Dateien wurden erfolgreich in die Datenbank geladen.")