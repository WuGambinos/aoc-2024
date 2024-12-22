import heapq
from collections import defaultdict
from copy import deepcopy
from queue import PriorityQueue

DIRECTIONS = [(0, -1, "L"), (0, 1, "R"), (-1, 0, "U"), (1, 0, "D")] 

f = open('../inputs/day16_test.txt', 'r')

def print_map(map):
    for row in map:
        print("".join(row))

def distance(a, b):
    r1, c1, _ = a
    r2, c2, _ = b

    return abs(c1-c2) + abs(r1-r2)


def reconstruct_path(came_from, current):
    total_path = [current]

    while current in came_from:
        current = came_from[current]
        total_path.append(current)

    return total_path[::-1]

"""
def find_path(maze, start, target):
    frontier = []
    heapq.heappush(frontier, (start, 0))

    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    r, c = start

    while frontier:
        curr = heapq.heappop(frontier)
        
        if curr == target:
            break


        for (dr, dc, dir) in DIRECTIONS:
            next_r, next_c = r + dr, c + dc
            next = (next_r, next_c)
            if next_r >= 0 and next_r < len(maze) and next_c >= 0 and next_c < len(maze[0]) and maze[next_r][next_c] != '#':
                new_cost = cost_so_far[curr] + distance(curr, next)

                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    heapq.heappush(frontier, (next, new_cost + distance(next, target)))
                    came_from[next] = curr


        return came_from, cost_so_far
"""
"""
def find_path(maze, start, target):
    open_set = []
    heapq.heappush(open_set, start)

    came_from = {}

    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0

    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = distance(start, start)

    while open_set:
        current = heapq.heappop(open_set)
        r, c , dir = current
        if (r, c) == target:
            return reconstruct_path(came_from, current)

        for (dr, dc, next_dir) in DIRECTIONS:
            next_r, next_c = r + dr, c + dc
            next = (next_r, next_c, next_dir)
            if next_r >= 0 and next_r < len(maze) and next_c >= 0 and next_c < len(maze[0]) and maze[next_r][next_c] != '#':
                h = 1 if dir == next_dir else 1000
                tent_g_score = g_score[current]  + h

                if tent_g_score < g_score[next]:
                    came_from[next] = current
                    g_score[next] = tent_g_score
                    #f_score[next] = tent_g_score + distance(current, next)
                    f_score[next] = tent_g_score + h
                    if next not in open_set:
                        heapq.heappush(open_set, next)

    return "FAILED"
"""



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


    r, c = start
    start = (r, c)
    result = find_path(maze, start, end)
    map = deepcopy(maze)


    if result != None:
        for (r, c) in result:
            map[r][c] = "L"

    print()
    print_map(map)
solve()
