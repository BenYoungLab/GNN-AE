def read_command(f):
    line = f.readline()
    if line != "":
        data = line.strip('\n').split('/n')
        sub_str = data[0].split(' ')
    else:
        return "finish"
    return sub_str


def Read_Graph(f):
    num_v, num_e = 0, 0
    nodes, node_labels, degrees, from_nodes, to_nodes, edge_labels = [], [], [], [], [], []
    graph_structure = {}
    sub_str = read_command(f)
    while sub_str[0] == 't':
        graph_structure.update({'num_v': int(sub_str[1])})
        graph_structure.update({'num_e': int(sub_str[2])})
        sub_str = read_command(f)
    while sub_str[0] == 'v':
        num_v = num_v + 1
        nodes.append(int(sub_str[1]))
        node_labels.append(int(sub_str[2]))
        degrees.append(int(sub_str[3]))
        sub_str = read_command(f)
    if num_v != graph_structure['num_v']:
        print("Error: num_v")
    graph_structure.update({'nodes': nodes, 'node_labels': node_labels, 'degrees': degrees})
    while sub_str[0] == 'e':
        num_e = num_e + 1
        from_nodes.append(int(sub_str[1]))
        to_nodes.append(int(sub_str[2]))
        sub_str = read_command(f)
    if num_e != graph_structure['num_e']:
        print("Error: num_e")
    graph_structure.update({'from_nodes': from_nodes, 'to_nodes': to_nodes})

    return graph_structure
