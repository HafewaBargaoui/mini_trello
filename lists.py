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
def add_list_to_board(board_dict, board_name):
    """Ajoute une nouvelle liste vide à un board donné."""
    if board_name in board_dict:
        board_dict[board_name].append([])  # Ajoute une liste vide
        print(f"Nouvelle liste ajoutée au board '{board_name}'.")
    else:
        print(f"Le board '{board_name}' n'existe pas.")



add_list_to_board(boards, "titi")

print(boards)