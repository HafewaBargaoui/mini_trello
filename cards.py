#rechercher list
def search_list(board_fils: dict, key_board: str) -> list:
    board_temp = board_fils
    return board_fils[key_board]

#ajout element
def add_element(list_parent: list, element_to_add: str | int | float) -> list:
    list_temp = list_parent
    list_temp.append(element_to_add)
    return list_temp

#suppression element
def suppr_element(list_parent: list, element_to_rem: str | int | float) -> list:
    list_temp = list_parent
    list_temp.remove(element_to_rem)
    return list_temp

#déplacement element entre lists
def depl_element(board_fils: dict, key1_from: str, key2_to: str, element_to_move: str | int | float) -> dict:
    dict_temp = board_fils
    (dict_temp.get(key1_from)).remove(element_to_move)
    (dict_temp.get(key2_to)).append(element_to_move)
    return dict_temp

#listing
def listing_element(list_show: list) -> None:
    print(f"list element: {list_show}")

# dict_test = {
#     "toto": [1,2,3,8],
#     "tata": [1,2,3,4],
#     "tutu": [1,2,3,4],
# }

# print(dict_test)
# print(search_list(dict_test, "toto"))
# dict_temp = add_element(search_list(dict_test,"toto"), 5)
# print(f"dict_temp apres add de 5= {dict_temp}")
# dict_temp = suppr_element(search_list(dict_test,"toto"),5)
# print(f"dict_temp apres supr de 5= {dict_temp}")
# dict_modif = depl_element(dict_test,"toto","tata",8)
# print(f"dict_temp apres depl de 8= {dict_modif}")