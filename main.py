import json

JSON_FILE = "mini_trello.json"

try:
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data_ent = json.load(f)
        print(f"Fichier '{JSON_FILE}' chargé dans la variable 'data_ent'.")
except FileNotFoundError:
    data_ent = {}  # Dictionnaire vide par défaut
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data_ent, f, ensure_ascii=False, indent=4)
    print(f"Fichier '{JSON_FILE}' créé avec un dictionnaire vide dans 'data_ent'.")

