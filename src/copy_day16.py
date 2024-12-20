from collections import deque
from copy import deepcopy

DIRECTIONS = [(0, -1, "L"), (0, 1, "R"), (-1, 0, "U"), (1, 0, "D")] 

f = open('../inputs/day16_test5.txt', 'r')

def print_map(map):
    for row in map:
        print("".join(row))


def remove_walls(map):
    first_adjusted_map = []
    for i in map:
        i.pop(0)
        first_adjusted_map.append(i)

    adjusted_map = []
    for i in first_adjusted_map:
        i.pop(len(i) - 1)
        adjusted_map.append(i)

    adjusted_map.pop(0)
    adjusted_map.pop(len(adjusted_map) - 1)
    return adjusted_map

ALL_PATHS = []

def reconstruct_path(end, TRACK):
    path = []
    curr = end
    dir_changes = 0
    while curr:
        path.append(curr)
        try:
            curr = TRACK[(curr[0], curr[1])]
        except KeyError:
            break

    path = path[::-1]
    #print("PATH")
    score = 0
    for (i, p) in enumerate(path):
        if i != len(path) - 1:
            if p[2] != 1:
                score += p[2]
        #print(p)
    #print("SCORE: ",score+len(path)-1)

    return (score+len(path)-1)

"""
TRACK = {}
def bfs(map, start_r, start_c, end):
    q = deque()
    visited = set()

    visited.add((start_r, start_c))
    q.append((start_r, start_c))

    # Iterate over q
    while q:
        curr = q.popleft()
        r, c = curr

        if (r, c) == end:
            break

        # Check Neighbors
        for (dr, dc) in DIRECTIONS:
            next_r, next_c = r + dr, c + dc

            if next_r >= 0 and next_r < len(map) and next_c >= 0 and next_c < len(map[0]) and map[next_r][next_c] != '#':
                if (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    q.append((next_r, next_c))
                    TRACK[(next_r, next_c)] = (r, c)
    """

def bfs(map, start_r, start_c, dir, end, TRACK):
    q = deque()
    visited = set()

    visited.add((start_r, start_c))
    q.append((start_r, start_c, dir))

    # Iterate over q
    while q:
        curr = q.popleft()
        r, c, curr_dir = curr

        if (r, c) == end:
            return curr

        # Check Neighbors
        for (dr, dc, next_dir) in DIRECTIONS:
            next_r, next_c = r + dr, c + dc

            valid = next_r >= 0 and next_r < len(map) and next_c >= 0 and next_c < len(map[0]) and map[next_r][next_c] != '#'
            if valid:
                cost = 1 if next_dir == curr_dir else 1000
                if (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    if cost == 1:
                        q.appendleft((next_r, next_c, next_dir))
                    else:
                        q.append((next_r, next_c, next_dir))
                    TRACK[(next_r, next_c)] = (r, c, cost)

def solve():

    map = []
    for line in f:
        map.append(list(line.strip()))
    print_map(map)

    new_map = remove_walls(map)
    print()
    print_map(new_map)

    start = None
    end = None

    for (i, row) in enumerate(new_map):
        for (j, cell) in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)

    print(f"START: {start} END: {end}")
    print()
    """
    path = [(start[0], start[1])]
    visited = set()
    visited.add((start[0], start[1]))

    res = find_path(new_map, start[0], start[1], end, visited, path)

    print(res)
    print(len(visited))
    """

    print("STARTING PATH FINDING")

    scores = []
    for (_, _, dir) in DIRECTIONS:
        (start_r, start_c) = start
        TRACK = {}
        res = bfs(new_map, start_r, start_c,dir, end, TRACK)
        score = reconstruct_path(end, TRACK)
        if dir != "R":
            score += 1000
        print(f"SCORE: {score} DIR: {dir}")
        scores.append(score)

    print(scores)
    print(min(scores))


solve()
