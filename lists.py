import json
# board_parent = {
#         "dict_test" : {
#             "toto": [1,2,3,4],
#             "tata": [1,2,3,4],
#             "tutu": [1,2,3,4],
#     },

#         "dict_test2" : {
#             "titi": [1,2,3,4],
#             "tyty": [1,2,3,4],
#             "toto": [1,2,3,4],
#     }
# }

def add_list_to_board(board_parent, board_name, key, new_list):
    """
    Ajoute une nouvelle liste sous la clé `key` dans le board `board_name` 
    du dictionnaire `board_parent`, si cette clé n'existe pas encore.
    """
    if board_name in board_parent:
        board = board_parent[board_name]
        if key not in board:
            board[key] = new_list
            print(f"Clé '{key}' ajoutée au board '{board_name}' avec la liste {new_list}.")
        else:
            print(f"La clé '{key}' existe déjà dans le board '{board_name}'.")
    else:
        print(f"Le board '{board_name}' n'existe pas.")


#add_list_to_board(board_parent, "dict_test2", "test", [1])

#print (board_parent )

def delete_list_from_board(board_parent, board_name, key):
    if board_name in board_parent:
        board = board_parent[board_name]
        if key in board:
            removed = board.pop(key)
            print(f"Clé '{key}' supprimée du board '{board_name}' : {removed}")
        else:
            print(f"La clé '{key}' n'existe pas dans le board '{board_name}'.")
    else:
        print(f"Le board '{board_name}' n'existe pas.")

#delete_list_from_board(board_parent, "dict_test2", "titi")


def list_lists_in_board(board_parent, board_name):
    """
    Affiche toutes les clés (listes) présentes dans le board donné.
    """
    if board_name in board_parent:
        board = board_parent[board_name]
        print(f"Listes dans le board '{board_name}' :")
        for list_name, content in board.items():
            print(f" - {list_name} : {content}")
    else:
        print(f"Le board '{board_name}' n'existe pas.")

# list_lists_in_board(board_parent, "dict_test2")