

node_dict = {'node_uuid': {'set_id1':1}, 'node_uuid2': {}}

uuid = 'node_uuid2'
paird_set_name = 'set_id1'


list_node_dict = list(node_dict.keys())


def print_eps_paired_to_node():
    global list_sets_in_dict
    for nodes in list_node_dict:
        if nodes == uuid :
            list_sets_in_dict = list(node_dict[nodes].keys())

            if paird_set_name in list_sets_in_dict:
                node_dict[nodes][paird_set_name] = node_dict[nodes][paird_set_name] + 1
            else:
                node_dict[nodes][paird_set_name] = 1


    for nodes in list_node_dict:
        print(f"{nodes}:")
        for sets,val in node_dict[nodes].items():


          print(" "*(len(nodes)+3),end = "")
          print(f"{sets} ----- {node_dict[nodes][sets]}")

if __name__ == "__main__":
    print_eps_paired_to_node()







