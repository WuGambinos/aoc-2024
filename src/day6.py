from helper import read_file_to_list
from copy import deepcopy

def print_map(map):
    for row in map:
        print(row)

guard_map = read_file_to_list("../inputs/day6_test.txt")

# Convert strings to list of chars
for (i, row) in enumerate(guard_map):
    guard_map[i] = list(row)

copy_guard_map = deepcopy(guard_map)


BLOCKER = "#"
OBSTRUCTION = "O"
NUM_ROWS = len(guard_map)
NUM_COLS = len(guard_map[0])

seen = []


# Clockwise
directions_char = ["^", ">", "v", "<"]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_guard_position_and_dir(map):
    for (i, row) in enumerate(map):
        for (j, cell) in enumerate(row):
            if (cell == '^' or cell == ">" or cell == "v" or cell == "<"):
                return ([i, j], directions_char.index(cell))
    return (None, None)

from enum import Enum

class Result(Enum):
    OutofMap = 1
    Blocker = 2
    Obstruction = 3



class Solution():
    def __init__(self):
        self.count = 0

    def part1(self):
        self.count = 0
        (init_pos, init_dir) = get_guard_position_and_dir(guard_map)
        print(f"GUARD POS: {init_pos} DIR: {init_dir}")
        s.traverse(guard_map, init_pos, init_dir)
        print("PART 1: ", s.count+2)
    
    def part2(self):
        self.count = 0
        (init_pos, init_dir) = get_guard_position_and_dir(copy_guard_map)
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.create_loop(copy_guard_map, init_pos, init_dir, r, c):
                    self.count += 1

        print_map(copy_guard_map)
        print("PART 2:", self.count)

# Movement Algorithm, 
# 1. if something in front, turn right 90 degress
# 2. otherwise step 
    def traverse(self, map, p, d):
        check = self.help_traverse(map, p, d)
        while check is not Result.OutofMap:
            d += 1
            d = d % 4
            map[p[0]][p[1]] = directions_char[d]
            check = self.help_traverse(map, p, d)
        print(self.count+2)
    
    def create_loop(self, map, p, d, r, c):
        #map[p[0]][p[1] - 1] = "O"
        map[r][c] = "O"
        check = self.help_traverse(map, p, d)
        while  check is not Result.OutofMap:
            print_map(map)
            print()
            d += 1
            d = d % 4
            map[p[0]][p[1]] = directions_char[d]
            check = self.help_traverse(map, p, d)
            if check == Result.Obstruction:
                map[r][c] = "."
                return True

        map[r][c] = "."
        return False

    def help_traverse(self, map, pos, dir):
        next_row = pos[0]  + directions[dir][0]
        next_col = pos[1] + directions[dir][1]

        if (next_row <= 0 or next_row >= NUM_ROWS - 1) or (next_col <= 0 or next_col >= NUM_COLS - 1):
            return Result.OutofMap

        while (map[next_row][next_col] is not BLOCKER and map[next_row][next_col] is not OBSTRUCTION):
            if (next_row <= 0 or next_row >= NUM_ROWS - 1) or (next_col <= 0 or next_col >= NUM_COLS - 1):
                return Result.OutofMap
            
            map[pos[0]][pos[1]] = "X"
            if (pos[0], pos[1]) not in seen:
                seen.append((pos[0], pos[1]))
                self.count += 1

            pos[0] = next_row
            pos[1] = next_col
            map[pos[0]][pos[1]] = directions_char[dir]
            next_row = pos[0]  + directions[dir][0]
            next_col = pos[1] + directions[dir][1]
        
        if map[next_row][next_col] is OBSTRUCTION:
            return Result.Obstruction
        
        return Result.Blocker



s = Solution()
s.part1()
s.part2()
