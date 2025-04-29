import json

def lecture_json() -> dict:
    pass

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

def suppression_boards() -> bool:
    pass 

def suppression_board(board_parent: dict, key_fils: str) -> dict:
    try:
        board_parent.pop(key_fils)
        return board_parent
    except:
        print("Clef non présente")
        return board_parent

def ajouter_board(board_parent: dict, key_fils: str, boards_fils: dict) -> dict:
    dict_temp = board_parent
    dict_temp[key_fils] = boards_fils
    return dict_temp

def listing_boards(dict_parent: dict) -> None:
    if not dict_parent == {}:
        for key,value in dict_parent.items():
            print(f"Key: {key} :::: Value: {value}")
    else:
        print("Dictionnaire vide")

dict_test = {
    "toto": [1,2,3,4],
    "tata": [1,2,3,4],
    "tutu": [1,2,3,4],
}

dict_parent = creation_board("board1_fils", dict_test)
listing_boards(dict_parent)

dict_parent = suppression_board(dict_parent, "board1_fils")
listing_boards(dict_parent)