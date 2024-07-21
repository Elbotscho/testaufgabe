import json
from faker import Faker
import random
from datetime import datetime

fake = Faker('de_DE')

# Anzahl der Datensätze
num_versicherte = 150
num_vertraege = 200
num_schadensfaelle = 100

# Listen zur Speicherung der generierten Daten
versicherte_daten = []
vertraege_daten = []
schadensfaelle_daten = []

# Generiere Versichertendaten
for i in range(num_versicherte):
    versicherte_daten.append({
        'versichertennummer': fake.unique.random_int(min=100000000, max=999999999),
        'name': fake.name(),
        'geburtsdatum': fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=100).isoformat(),
        'adresse': fake.address()
    })

# Generiere Versicherungsverträge
for i in range(num_vertraege):
    versichertennummer = random.choice(versicherte_daten)['versichertennummer']
    start_date = fake.date_between(start_date='-5y', end_date='today')
    end_date = fake.date_between(start_date=start_date, end_date='+5y') if random.choice([True, False]) else None
    
    if end_date and end_date < datetime.today().date():
        vertragsstatus = 'abgelaufen'
    else:
        vertragsstatus = random.choice(['aktiv', 'gekündigt', 'abgelaufen'])

    vertraege_daten.append({
        'vertragsnummer': fake.unique.random_int(min=100000000, max=999999999),
        'versichertennummer': versichertennummer,
        'vertragsbeginn': start_date.isoformat(),
        'vertragsende': end_date.isoformat() if end_date else None,
        'vertragsstatus': vertragsstatus
    })

# Generiere Schadensfalldaten
for i in range(num_schadensfaelle):
    vertragsdaten = random.choice(vertraege_daten)

    vertragsnummer = vertragsdaten['vertragsnummer']
    vertragsbeginn = datetime.strptime(vertragsdaten['vertragsbeginn'], '%Y-%m-%d').date()
    schaden_date = fake.date_between(start_date=vertragsbeginn, end_date='today')
    schaden_typ = random.choice(['Unfall', 'Diebstahl', 'Feuer'])
    schaden_hoehe = round(random.uniform(10, 10000), 2)  

    schadensfaelle_daten.append({
        'schadensnummer': fake.unique.random_int(min=100000000, max=999999999),
        'vertragsnummer': vertragsnummer,
        'datum': schaden_date.isoformat(),
        'schadenstyp': schaden_typ,
        'schadenhoehe': schaden_hoehe
    })

# Speichern der Versichertendaten in einer JSON-Datei
with open('versicherte_daten.json', 'w') as json_file:
    json.dump(versicherte_daten, json_file, indent=4)

# Speichern der Versicherungsverträge in einer JSON-Datei
with open('vertraege_daten.json', 'w') as json_file:
    json.dump(vertraege_daten, json_file, indent=4)

# Speichern der Schadensfalldaten in einer JSON-Datei
with open('schadensfaelle_daten.json', 'w') as json_file:
    json.dump(schadensfaelle_daten, json_file, indent=4)

print("Daten wurden erfolgreich in 'versicherte_daten.json', 'vertraege_daten.json' und 'schadensfaelle_daten.json' gespeichert.")
