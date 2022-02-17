# File: Lab11.py - Timothy Wang

import math


def PrimMST(G):
    """G is represented as an adjacency matrix"""

    # initializes a list of the smallest weight edge connecting that vertex
    minimum_weights = list(999999999999 for x in range(len(G)))

    # initializes a list of the preceding node of the current node
    connections = list(None for x in range(len(G)))

    # initializes starting node as 0, no parent node as it is the head of the tree
    minimum_weights[0] = 0
    included = set()

    for x in range(len(G)):

        # finds the closest node in the graph that
        closest_value = 9999999999999999
        closest_node = None
        for y in range(len(G)):
            if minimum_weights[y] < closest_value and y not in included:
                closest_value = minimum_weights[y]
                closest_node = y

        included.add(closest_node)

        for y in range(len(G)):
            if G[closest_node][y] > 0 and y not in included and G[closest_node][y] < minimum_weights[y]:
                minimum_weights[y] = G[closest_node][y]
                connections[y] = closest_node

    return list(sorted([x, connections[x]]) + [minimum_weights[x]] for x in range(len(G)))


def test1():
    matrix = [[0, 7, 0, 5, 0, 0, 0],
              [7, 0, 8, 9, 7, 0, 0],
              [0, 8, 0, 0, 5, 0, 0],
              [5, 9, 0, 0, 15, 6, 0],
              [0, 7, 5, 15, 0, 8, 9],
              [0, 0, 0, 6, 8, 0, 11],
              [0, 0, 0, 0, 9, 11, 0]]
    min_tree = PrimMST(matrix)
    print('Edge        Weight')

    total = 0
    for x in range(7):
        if min_tree[x][1] is not None and min_tree[x][0] is not None:
            print('({}, {})       {}'.format(
                min_tree[x][0], min_tree[x][1], min_tree[x][2]))
            total += min_tree[x][2]
    print('MST Weight: {}'.format(total))


test1()
