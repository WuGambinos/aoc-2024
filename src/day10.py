
from enum import Enum
from collections import deque

def print_map(map):
    for row in map:
        print(row)


def dfs(matrix):

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    stack = [(0, 0, [(0, 0)])]
    #visited = [(0, 0)]

    while stack:
        x, y, path = stack.pop()

        if x < 0 or y < 0 or x >= rows or y >= cols or matrix[x][y] == 0 or visited[x][y]:
            continue

        if x == rows - 1 and y == cols - 1:
            print_map(visited)
            return path


        visited[x][y] = True
        stack.append((x + 1, y, path + [(x+1, y)]))
        stack.append((x - 1, y, path + [(x-1), y]))
        stack.append((x, y + 1, path + [(x, y+1)]))
        stack.append((x, y - 1, path + [(x, y-1)]))


    return []


def solve():
    f = open('../inputs/day10_test.txt')
    topo_map = []
    for line in f:
        inner = [int(n) for n in list(line.strip())]
        topo_map.append(inner)

    print_map(topo_map)
    
    """
    for (i, row) in enumerate(topo_map):
        for (j, cell) in enumerate(row):
            if (cell == 0):
                print(search(topo_map, i, j, None))
            break
    """
    print()
    matrix =  [
            [1, 0, 1, 1], 
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 1, 1],
            ]
    print_map(matrix)
    found = dfs(matrix)
    print(found)
solve()
