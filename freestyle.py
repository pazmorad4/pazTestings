

node_dict = {'node_uuid': {'set_id1': 0, 'set_id2': 0, 'set_id3': 0}, 'node_uuid2': {'set_id1': 0, 'set_id2': 0, 'set_id3': 0}}

uuid = 'node_uuid2'
set_name = 'set_id1'
#my_set_list = ['set_id2', 'set_id3'] # this wont be a list in the real code it wil be a string that i get from db node_uuid
list_node_dict = list(node_dict.keys())

#is it comit
def print_eps_paired_to_node():
    for nodes in list_node_dict:
        if nodes == uuid:
            list_sets_in_dict = list(node_dict[nodes].keys())
            for sets in list_sets_in_dict:
                if sets == set_name:
                    node_dict[nodes][sets] = node_dict[nodes][sets] + 1

    for nodes in list_node_dict:
        print(f"{nodes}  :")
        for sets in list_sets_in_dict:
            print(f"{sets} ----- {node_dict[nodes][sets]}")

if __name__ == "__main__":
    print_eps_paired_to_node()




