import time

from read_graph import *
from output import *

# param
data_graph = 'ws'
generate_graphs = 100
rw_lengths = [4, 6, 8, 10, 12, 16, 24, 32]  # query size |V(Q)|
rw_break = 500
sample_break = 500
rw_direction_dense = 3
rw_direction_sparse = 1
rw_direction = 2
real_graphs = ['yeast', 'hprd', 'wordnet', 'dblp', 'youtube', 'patents']
synthetic_graphs = ['rg', 'ws', 'ba']

# read
start = time.time()
file = open('datasets/' + data_graph + '.graph', "r")
graph_structure = Read_Graph(file)
file.close()
print("Finish reading!")

# ready data
G = nx.Graph()
G.add_nodes_from(graph_structure['nodes'])
G_edges = []
for i in range(graph_structure['num_e']):
    G_edges.append((graph_structure['from_nodes'][i], graph_structure['to_nodes'][i]))
G.add_edges_from(G_edges)

if data_graph in real_graphs:
    real_queries(rw_lengths, generate_graphs, graph_structure, G, rw_direction_dense,
                 rw_direction_sparse, sample_break, rw_break, data_graph)
elif data_graph in synthetic_graphs:
    synthetic_queries(rw_lengths, generate_graphs, graph_structure, G, sample_break,
                      rw_break, rw_direction, data_graph)
else:
    print('Error: no this dataset!')
