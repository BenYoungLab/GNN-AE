import random
import numpy as np


def RandomWalk_dense(G, length, current_node, rw_break, rw_direction):
    path = set()
    path.add(current_node)
    node_list = list(G.neighbors(current_node))
    direct_current_node = random.sample(node_list, rw_direction)
    for node in direct_current_node:
        path.add(node)
    step = 0
    while len(path) < length and step < rw_break:
        for i in range(rw_direction):
            node_list = list(G.neighbors(direct_current_node[i]))
            direct_node = np.random.choice(node_list)
            path.add(direct_node)
            direct_current_node[i] = direct_node
            step += 1
    if len(list(path)) > length:
        result = list(path)[0:length]
    else:
        result = list(path)

    return result


def RandomWalk_sparse(G, length, current_node, rw_break, rw_direction):
    path = set()
    path.add(current_node)
    direct_current_node = [current_node] * rw_direction
    step = 0
    while len(path) < length and step < rw_break:
        for i in range(rw_direction):
            node_list = list(G.neighbors(direct_current_node[i]))
            direct_node = np.random.choice(node_list)
            path.add(direct_node)
            direct_current_node[i] = direct_node
            step += 1
    if len(list(path)) > length:
        result = list(path)[0:length]
    else:
        result = list(path)

    return result


def RandomWalk(G, length, current_node, rw_break, rw_direction):
    path = set()
    path.add(current_node)
    direct_current_node = [current_node] * rw_direction
    step = 0
    while len(path) < length and step < rw_break:
        for i in range(rw_direction):
            node_list = list(G.neighbors(direct_current_node[i]))
            direct_node = np.random.choice(node_list)
            path.add(direct_node)
            direct_current_node[i] = direct_node
            step += 1
    if len(list(path)) > length:
        result = list(path)[0:length]
    else:
        result = list(path)

    return result