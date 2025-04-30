import json

boards = {
    "titi": [
        [1, 2, 3],        
        [4, 5],            
    ],
    "haha": [
        [7, 8, 9],
        [10],
        [10, 11, 0]
    ],
    "kiki": [
        [9, 77, 5],
        []
    ]
}
def add_list_to_board(board_dict, board_name, new_list):
 """
    Ajoute une nouvelle liste (fournie en paramètre) à un board donné.
     
    :param board_dict: Le dictionnaire contenant tous les boards.
    :param board_name: Le nom du board auquel ajouter la liste.
    :param new_list: La liste à ajouter (ex: [42, 43]).
    """
 if board_name in board_dict:
        board_dict[board_name].append(new_list)  
        print(f"Nouvelle liste ajoutée au board '{board_name}'.")
 else:
        print(f"Le board '{board_name}' n'existe pas.")



add_list_to_board(boards, "titi4", [5,777777])


print(boards)