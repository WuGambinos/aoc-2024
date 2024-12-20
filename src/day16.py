import heapq

DIRECTIONS = [(0, -1, "L"), (0, 1, "R"), (-1, 0, "U"), (1, 0, "D")] 

f = open('../inputs/day16_test.txt', 'r')

def print_map(map):
    for row in map:
        print("".join(row))

def solve():

    maze = []
    for line in f:
        maze.append(list(line.strip()))
    print_map(maze)


    start = None
    end = None

    for (i, row) in enumerate(maze):
        for (j, cell) in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
solve()
