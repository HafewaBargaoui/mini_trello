import boards

JSON_FILE = "mini_trello.json"

dict_test = {
    "toto": [1,2,3,4],
    "tata": [1,2,3,4],
    "tutu": [1,2,3,4],
}

dict_test2 = {
    "titi": [1,2,3,4],
    "tyty": [1,2,3,4],
    "toto": [1,2,3,4],
}
print("="*40)
boards.create_json(JSON_FILE)
print("="*40)
boards.modify_json(JSON_FILE,boards.creation_board("Board1_fils", dict_test))
print("="*40)
boards.listing_boards(boards.get_json(JSON_FILE))
print("="*40)
data_temp = boards.ajouter_board(boards.get_json(JSON_FILE), "Board2_fils", dict_test2)
print("="*40)
boards.listing_boards(boards.get_json(JSON_FILE))
print("="*40)
data_temp = boards.suppression_board(data_temp, "Board1_fils")
print("="*40)
boards.listing_boards(data_temp)
print("="*40)
boards.modify_json(JSON_FILE, data_temp)
print("="*40)
boards.suppression_boards(JSON_FILE)
