from collections import deque
from copy import deepcopy

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)] 

f = open('../inputs/day16.txt', 'r')

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
    prev = end
    curr = end
    prev_dir = (curr[0] - prev[0], curr[1] - prev[1])
    dir_changes = 0
    while curr:
        path.append(curr)
        try: 
            curr = TRACK[curr]
            curr_dir = (curr[0] - prev[0], curr[1] - prev[1])
            if curr_dir != prev_dir:
                dir_changes += 1

            prev = curr
            prev_dir = curr_dir
        except KeyError:
            break

    print("DIRECTION CHANGES", dir_changes)
    return (dir_changes, path[::-1])

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

TRACK = {}
def bfs(map, dir, start_r, start_c, end):
    q = deque()
    visited = set()

    visited.add((start_r, start_c))
    q.append((start_r, start_c, dir))

    # Iterate over q
    while q:
        curr = q.popleft()
        r, c, curr_dir = curr

        if (r, c) == end:
            break

        # Check Neighbors
        for (i, (dr, dc)) in enumerate(DIRECTIONS):
            next_r, next_c = r + dr, c + dc

            valid = next_r >= 0 and next_r < len(map) and next_c >= 0 and next_c < len(map[0]) and map[next_r][next_c] != '#'
            if valid:
                cost = 0 if i == curr_dir else 1
                if (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    if cost == 0:
                        q.appendleft((next_r, next_c, i))
                    else:
                        q.append((next_r, next_c, i))
                    TRACK[(next_r, next_c)] = (r, c)

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
    for i in range(len(DIRECTIONS)):
        bfs(new_map, i, start[0], start[1], end)
        print()

    dir_changes, path = reconstruct_path(end, TRACK)
    print("STEPS: ", len(path) - 1, path)

    score = dir_changes * 1000 + len(path) - 1
    print("SCORE: ", score)




solve()
