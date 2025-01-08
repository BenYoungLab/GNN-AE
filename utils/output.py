import os
import networkx as nx

from random_walk import *


def format_trans(induced_subgraph, graph_structure):
    num_v = len(induced_subgraph.nodes)
    num_e = len(induced_subgraph.edges)
    nodes = list(induced_subgraph.nodes)
    nodes_new = [n for n in range(num_v)]
    node_labels = [graph_structure['node_labels'][node] for node in nodes]
    degrees = [induced_subgraph.degree[node] for node in nodes]
    from_nodes = [list(induced_subgraph.edges)[k][0] for k in range(len(induced_subgraph.edges))]
    to_nodes = [list(induced_subgraph.edges)[k][1] for k in range(len(induced_subgraph.edges))]
    from_nodes_new = [nodes.index(from_node) for from_node in from_nodes]
    to_nodes_new = [nodes.index(to_node) for to_node in to_nodes]
    edge_labels = [0] * num_e
    query_structure = {'num_v': num_v, 'num_e': num_e, 'nodes': nodes_new, 'node_labels': node_labels,
                       'degrees': degrees, 'from_nodes': from_nodes_new, 'to_nodes': to_nodes_new,
                       'edge_labels': edge_labels}

    return query_structure


def output(file_name, query):
    with open(file_name, "w") as output_query:
        output_query.write('t ' + str(query['num_v']) + ' ' + str(query['num_e']) + '\n')
        for v in range(query['num_v']):
            output_query.write('v ' + str(query['nodes'][v]) + ' ' + str(query['node_labels'][v]) + \
                               ' ' + str(query['degrees'][v]) + '\n')
        for e in range(int(query['num_e'])):
            output_query.write('e ' + str(query['from_nodes'][e]) + ' ' + str(query['to_nodes'][e]) + \
                               ' ' + str(query['edge_labels'][e]) + '\n')
    output_query.close()


def real_queries(rw_lengths, generate_graphs, graph_structure, G, rw_direction_dense,
                 rw_direction_sparse, sample_break, rw_break, data_graph):
    # extract
    for rw_length in rw_lengths:
        print("-------------------------------")
        print("Current query size: ", rw_length)
        dense_graphs, sparse_graphs = [], []
        if rw_length >= 6:
            while len(dense_graphs) < generate_graphs:
                # random area
                random_node = np.random.choice(graph_structure['nodes'])
                while len(list(G.neighbors(int(random_node)))) < rw_direction_dense:
                    random_node = np.random.choice(graph_structure['nodes'])

                sample_num, extract_flag = 0, 0
                while sample_num < sample_break and extract_flag == 0:
                    # dense random walk
                    rw_path = RandomWalk_dense(G, rw_length, int(random_node), rw_break, rw_direction_dense)
                    if len(rw_path) < rw_length:
                        sample_num += 1
                        continue
                    else:
                        induced_subgraph = nx.subgraph(G, rw_path)
                        avg_degree = sum([induced_subgraph.degree[key] for key in list(induced_subgraph.nodes)]) / len(
                                     induced_subgraph.nodes)
                        if_connect = nx.is_connected(induced_subgraph)
                        if if_connect and avg_degree > 3:
                            dense_graphs.append(induced_subgraph)
                            extract_flag = 1
                        sample_num += 1
                print("Current number of dense graphs: ", len(dense_graphs))

        while len(sparse_graphs) < generate_graphs:
            # random area
            random_node = np.random.choice(graph_structure['nodes'])
            while len(list(G.neighbors(int(random_node)))) == 0:  # there are some isolate nodes in the data graph
                random_node = np.random.choice(graph_structure['nodes'])

            sample_num, extract_flag = 0, 0
            while sample_num < sample_break and extract_flag == 0:
                # dense random walk
                rw_path = RandomWalk_sparse(G, rw_length, int(random_node), rw_break, rw_direction_sparse)
                if len(rw_path) < rw_length:
                    sample_num += 1
                    continue
                else:
                    induced_subgraph = nx.subgraph(G, rw_path)
                    avg_degree = sum([induced_subgraph.degree[key] for key in list(induced_subgraph.nodes)]) / len(
                        induced_subgraph.nodes)
                    if_connect = nx.is_connected(induced_subgraph)
                    if if_connect and avg_degree <= 3:
                        sparse_graphs.append(induced_subgraph)
                        extract_flag = 1
                    sample_num += 1
            print("Current number of sparse graphs: ", len(sparse_graphs))

        # query format transform for output
        out_dense_graphs, out_sparse_graphs = [], []
        for i in range(len(dense_graphs)):
            query_structure = format_trans(dense_graphs[i], graph_structure)
            out_dense_graphs.append(query_structure)
        for i in range(len(sparse_graphs)):
            query_structure = format_trans(sparse_graphs[i], graph_structure)
            out_sparse_graphs.append(query_structure)
        print("The total number of dense queries: ", len(out_dense_graphs))
        print("The total number of sparse queries: ", len(out_sparse_graphs))

        # output
        out_path = 'datasets/' + data_graph + '_queries/'
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        for i in range(len(out_sparse_graphs)):
            file_name = 'query_sparse_' + str(rw_length) + '_' + str(i + 1) + '.graph'
            file_name = out_path + file_name
            output(file_name, out_sparse_graphs[i])
        for i in range(len(out_dense_graphs)):
            file_name = 'query_dense_' + str(rw_length) + '_' + str(i + 1) + '.graph'
            file_name = out_path + file_name
            output(file_name, out_dense_graphs[i])


def synthetic_queries(rw_lengths, generate_graphs, graph_structure, G, sample_break,
                      rw_break, rw_direction, data_graph):
    # extract
    for rw_length in rw_lengths:
        print("-------------------------------")
        print("Current query size: ", rw_length)
        query_graphs = []
        while len(query_graphs) < generate_graphs:
            # random area
            random_node = np.random.choice(graph_structure['nodes'])
            while len(list(G.neighbors(int(random_node)))) == 0:  # there are some isolate nodes in the data graph
                random_node = np.random.choice(graph_structure['nodes'])

            sample_num, extract_flag = 0, 0
            while sample_num < sample_break and extract_flag == 0:
                # dense random walk
                rw_path = RandomWalk(G, rw_length, int(random_node), rw_break, rw_direction)
                if len(rw_path) < rw_length:
                    sample_num += 1
                    continue
                else:
                    induced_subgraph = nx.subgraph(G, rw_path)
                    avg_degree = sum([induced_subgraph.degree[key] for key in list(induced_subgraph.nodes)]) / len(
                        induced_subgraph.nodes)
                    if_connect = nx.is_connected(induced_subgraph)
                    if if_connect:
                        query_graphs.append(induced_subgraph)
                        extract_flag = 1
                    sample_num += 1
            print("Current number of graphs: ", len(query_graphs))

        # query format transform for output
        out_graphs = []
        for i in range(len(query_graphs)):
            query_structure = format_trans(query_graphs[i], graph_structure)
            out_graphs.append(query_structure)
        print("The total number of queries: ", len(out_graphs))

        # output
        out_path = 'datasets/' + data_graph + '_queries/'
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        for i in range(len(out_graphs)):
            file_name = 'query_' + str(rw_length) + '_' + str(i + 1) + '.graph'
            file_name = out_path + file_name
            output(file_name, out_graphs[i])