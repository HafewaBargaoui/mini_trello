import boards
import lists
import cards

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

print("#creation du JSON")
boards.create_json(JSON_FILE) 
print("="*40)
print("="*40)
print("="*40)

print("#modification du JSON (ajout d'un dictionnaire dans le fichier)")
boards.modify_json(JSON_FILE,boards.creation_board("Board1_fils", dict_test)) 
print("="*40)
print("="*40)
print("="*40)

print("#listing du contenu du JSON")
boards.listing_boards(boards.get_json(JSON_FILE)) 
print("="*40)
print("="*40)
print("="*40)

print("#ajout d'un board")
data_temp = boards.ajouter_board(boards.get_json(JSON_FILE), "Board2_fils", dict_test2) 
print("="*40)
print("="*40)
print("="*40)

# print("#modification du fichier JSON")
# boards.modify_json(JSON_FILE, data_temp) 
# print("="*40)
# print("="*40)
# print("="*40)

print("#ajout list dans un board")
lists.add_list_to_board(data_temp, "Board2_fils", "tutu", [2,3,8,4])
print("="*40)
print("="*40)
print("="*40)

# print("#modification du fichier JSON")
# boards.modify_json(JSON_FILE, data_temp) 
# print("="*40)
# print("="*40)
# print("="*40)

print("#suppression list dans un board")
lists.delete_list_from_board(data_temp, "Board1_fils", "toto")
print("="*40)
print("="*40)
print("="*40)

# print("#modification du fichier JSON")
# boards.modify_json(JSON_FILE, data_temp) 
# print("="*40)
# print("="*40)
# print("="*40)

print("#listing au sein d'un board")
lists.list_lists_in_board(data_temp, "Board2_fils")
print("="*40)
print("="*40)
print("="*40)

print("#Ajout élément à une list d'un board")
cards.add_element(cards.search_list(cards.search_list(data_temp, "Board2_fils"),"titi"),37)
print("="*40)
print("="*40)
print("="*40)

print("#listing du contenu du board parent")
boards.listing_boards(data_temp)
print("="*40)
print("="*40)
print("="*40)

print("#Suppr élément à une list d'un board")
cards.suppr_element(cards.search_list(cards.search_list(data_temp, "Board2_fils"),"titi"),37)
print("="*40)
print("="*40)
print("="*40)

print("#listing du contenu du board parent")
boards.listing_boards(data_temp)
print("="*40)
print("="*40)
print("="*40)

print("#deplacement entre lists")
cards.depl_element(cards.search_list(data_temp, "Board2_fils"),"titi","tyty",4)
print("="*40)
print("="*40)
print("="*40)

print("#listing du contenu du board parent")
boards.listing_boards(data_temp)
print("="*40)
print("="*40)
print("="*40)

print("#listing element dans une list d'un board")
cards.listing_element(cards.search_list(cards.search_list(data_temp, "Board2_fils"),"titi"))
print("="*40)
print("="*40)
print("="*40)

# print("#clear du fichier JSON")
# boards.suppression_boards(JSON_FILE)
