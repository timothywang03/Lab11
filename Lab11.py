# File: Lab11.py - Timothy Wang

import math


def PrimMST(G):
    """G is represented as an adjacency matrix"""
    keys = dict()
    for x in range(len(G)):
        keys[x] = [99999999999, None]   # some arbitrary very large value

    queue = set()
    cur = 0

    while len(queue) < len(G):
        for x in range(len(G)):
            if G[cur][x] != 0:  # if there exists an edge between cur and x
                if x not in queue and G[cur][x] < keys[cur][0]:
                    keys[cur][1] = x
                    keys[cur][0] = G[cur][x]
        queue.add(cur)

        closest = 99999999999999
        for x in range(len(G)):
            if G[x][0] < closest and x not in queue:
                cur = x
                closest = keys[x][0]
        print(keys)

    return keys


def test1():
    matrix = list(list(0 for x in range(7)) for y in range(7))
    matrix[0][1] = 7
    matrix[1][0] = 7
    matrix[1][2] = 8
    matrix[2][1] = 8
    matrix[0][3] = 5
    matrix[3][0] = 5
    matrix[1][3] = 9
    matrix[3][1] = 9
    matrix[1][4] = 7
    matrix[4][1] = 7
    matrix[2][4] = 5
    matrix[4][2] = 5
    matrix[3][4] = 15
    matrix[4][3] = 15
    matrix[3][5] = 6
    matrix[5][3] = 6
    matrix[5][6] = 11
    matrix[6][5] = 11
    matrix[6][4] = 9
    matrix[4][6] = 9
    matrix[4][5] = 8
    matrix[5][4] = 8
    min_tree = PrimMST(matrix)
    print('Edge       Weight')
    for x in range(7):
        print('({}, {})       {}'.format(min_tree[x][1], x, min_tree[x][0]))


def test2():
    matrix = [[0, 7, 0, 5, 0, 0, 0],
              [7, 0, 8, 9, 7, 0, 0],
              [0, 8, 0, 0, 5, 0, 0],
              [5, 9, 0, 0, 15, 6, 0],
              [0, 7, 5, 15, 0, 8, 9],
              [0, 0, 0, 6, 8, 0, 11],
              [0, 0, 0, 0, 9, 11, 0]]
    min_tree = PrimMST(matrix)
    print('Edge        Weight')
    committed = list()
    for x in range(7):
        if min_tree[x][1] not in committed or x not in committed:
            print('({}, {})       {}'.format(
                min_tree[x][1], x, min_tree[x][0]))
            committed.append(min_tree[x][1])
            committed.append(x)


test2()
