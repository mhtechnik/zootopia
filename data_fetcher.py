import os
from pathlib import Path

import requests
from dotenv import load_dotenv

API_URL = "https://api.api-ninjas.com/v1/animals"

# Pfad zur .env anhand des Dateistandorts bestimmen
BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / ".env"

# .env laden
load_dotenv(dotenv_path=env_path)


API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """
    Holt die Tierdaten für 'animal_name' aus der API.
    Rückgabe: Liste von Dictionaries (kann auch leer sein).
    """
    if not API_KEY:
        print(f"Fehler: API_KEY ist nicht gesetzt. Gesucht wurde in {env_path}")
        return []

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)
    except requests.RequestException as e:
        print("Fehler bei der Anfrage:", e)
        return []

    if response.status_code != 200:
        print(f"Fehler: Statuscode {response.status_code}")
        return []

    data = response.json()
    if not isinstance(data, list):
        return []

    return data
