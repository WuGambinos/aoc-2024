
from enum import Enum
from collections import deque

def print_map(map):
    for row in map:
        print(row)

def solve():
    f = open('../inputs/day10_test.txt')
    topo_map = []
    for line in f:
        inner = [int(n) for n in list(line.strip())]
        topo_map.append(inner)
    
    """
    for (i, row) in enumerate(topo_map):
        for (j, cell) in enumerate(row):
            if (cell == 0):
                print(search(topo_map, i, j, None))
            break
    """