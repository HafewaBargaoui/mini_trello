import json

def create_json(json_file: str) -> dict:
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data_ent = json.load(f)
            print(f"Fichier '{json_file}' chargé dans la variable 'data_ent'.")
            return data_ent
    except FileNotFoundError:
        data_ent = {}  # Dictionnaire vide par défaut
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data_ent, f, ensure_ascii=False, indent=4)
        print(f"Fichier '{json_file}' créé avec un dictionnaire vide.")
        return data_ent

def get_json(json_file: str) -> dict:
    with open(json_file, 'r', encoding='utf-8') as f:
        data_ent = json.load(f)
        print(f"Fichier '{json_file}' chargé dans la variable 'data_ent'.")
    
    return data_ent

def modify_json(json_file: str, dict_data: dict) -> bool:
    try:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(dict_data, f, ensure_ascii=False, indent=4)
        print(f"Fichier '{json_file}' modifié.")
    except:
        return False

def creation_board(key_fils: str, boards_fils: dict) -> dict:
    """Creation du board parent

    Args:
        key_fils (str): chaine de caractère contenant la clé du board
        boards_fils (dict): board

    Returns:
        dict: retourne le dictionnaire parent
    """
    dict_parent = {}
    dict_parent[key_fils] = boards_fils
    return dict_parent

def suppression_boards(json_file: str) -> bool:
    try:
        mini_trello_empty = {}
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(mini_trello_empty, f, ensure_ascii=False, indent=4)
        print(f"Fichier '{json_file}' vidé.")
    except:
        print(f"Le fichier n'existe pas")

def suppression_board(board_parent: dict, key_fils: str) -> dict:
    try:
        print(f"Suppression du board : clef:{key_fils}")
        board_parent.pop(key_fils)
        return board_parent
    except:
        print("Clef non présente")
        return board_parent

def ajouter_board(board_parent: dict, key_fils: str, boards_fils: dict) -> dict:
    try:
        print(f"Ajout du board : {boards_fils}")
        dict_temp = board_parent
        dict_temp[key_fils] = boards_fils
        print(f"Nouveau board: {dict_temp}")
        return dict_temp
    except:
        print("Clef non présente")
        return board_parent

def listing_boards(dict_parent: dict) -> None:
    if not dict_parent == {}:
        for key,value in dict_parent.items():
            print(f"Key: {key} :::: Value: {value}")
    else:
        print("Dictionnaire vide")
