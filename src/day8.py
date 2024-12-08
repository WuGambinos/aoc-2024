from copy import deepcopy

MARKER = '#'
EMPTY = '.'

class Antenna:
    def __init__(self, id, y, x):
        self.id = id
        self.y = y
        self.x = x
    
    def print(self):
        print(f"ID: {self.id} X: {self.x} Y: {self.y}")

def print_map(map, as_str):
    if as_str:
        for row in map:
            print("".join(row))
    else:
        for row in map:
            print(row)


def is_antenna(ch):
    return ch.isalpha() or ch.isdigit()


def solve(part1):
    f = open('../inputs/day8.txt')
    map = []
    antenna_list = []

    # Convert list of strings to list of char list
    for line in f:
        map.append(list(line.strip()))

    NUM_COLS = len(map[0])
    NUM_ROWS = len(map)

    # Collect List of Antennas
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if is_antenna(map[i][j]):
                antenna_list.append(Antenna(map[i][j], i, j))
    
    copy_map = deepcopy(map)
    track = []

    for i in range(len(antenna_list) - 1):
        antenna1 = antenna_list[i]
        for j in range(i+1, len(antenna_list)):
            antenna2 = antenna_list[j]
            if antenna1.id == antenna2.id:

                # Parts of slope
                delta_y = (antenna2.y - antenna1.y) 
                delta_x = (antenna2.x - antenna1.x) 
                #m =(antenna2.y - antenna1.y) / (a2.x - a1.x) 
                track.append((antenna1, antenna2, delta_x, delta_y))

    unique = 0
    if part1:
        unique =  0
    else:
        unique = len(antenna_list)

    for (i, antenna_info) in enumerate(track):
        a1, a2, delta_x, delta_y = antenna_info

        # First Slope
        y1 = a1.y - delta_y
        x1 = a1.x - delta_x
        condition1 = (y1 >= 0 and x1 >= 0) and (y1 < NUM_ROWS and x1 < NUM_COLS)
        if part1:
            if condition1:
                if copy_map[y1][x1] != MARKER: 
                    unique += 1
                    copy_map[y1][x1] = MARKER
        else:
            while condition1:
                condition1 = (y1 >= 0 and x1 >= 0) and (y1 < NUM_ROWS and x1 < NUM_COLS)
                if condition1:
                    if copy_map[y1][x1] is not MARKER and copy_map[y1][x1] is EMPTY: 
                        unique += 1
                        copy_map[y1][x1] = MARKER
                y1 -= delta_y
                x1 -= delta_x

        # Second Slope
        y2 = a2.y + delta_y
        x2 = a2.x + delta_x
        condition2 = (y2 >= 0 and x2 >= 0) and (y2 < NUM_ROWS and x2 < NUM_COLS)
        if part1:
            if condition2:
                if copy_map[y2][x2] != MARKER:
                    unique += 1
                    copy_map[y2][x2] = MARKER
        else:
            while condition2:
                condition2 = (y2 >= 0 and x2 >= 0) and (y2 < NUM_ROWS and x2 < NUM_COLS)

                if  condition2:
                    if copy_map[y2][x2] is not MARKER and copy_map[y2][x2] is EMPTY:
                        unique += 1
                        copy_map[y2][x2] = MARKER
                y2 += delta_y
                x2 += delta_x
    
    print_map(copy_map, True)
    if part1:
        print("PART 1: ", unique)
        print()
    else:
        print("PART 2: ", unique)
        print()



solve(True)
solve(False)
