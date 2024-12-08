from copy import deepcopy

MARKER = '#'

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

def part1():
    f = open('../inputs/day8_test2.txt')
    map = []
    antenna_list = []
    for line in f:
        map.append(list(line.strip()))

    NUM_COLS = len(map[0])
    NUM_ROWS = len(map)
    print(f"NUM ROWS: {NUM_ROWS} NUM_COLS: {NUM_COLS}")

    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if is_antenna(map[i][j]):
                antenna_list.append(Antenna(map[i][j], i, j))
    
    copy_map = deepcopy(map)

    track = []

    for i in range(len(antenna_list) - 1):
        a1 = antenna_list[i]
        for j in range(i+1, len(antenna_list)):
            a2 = antenna_list[j]
            if a1.id == a2.id:
                delta_y = (a2.y - a1.y) 
                delta_x = (a2.x - a1.x) 
                #m =(a2.y - a1.y) / (a2.x - a1.x) 
                track.append((a1, a2, delta_x, delta_y))
    print()


    unique = 0
    for antenna_info in track:
        a1, a2, delta_x, delta_y = antenna_info

        y1 = a1.y - delta_y
        x1 = a1.x - delta_x
        y2 = a2.y + delta_y
        x2 = a2.x + delta_x

        if (y1 >= 0 and x1 >= 0) and (y1 < NUM_ROWS and x1 < NUM_COLS):
            if copy_map[y1][x1] != MARKER:
                unique += 1
                copy_map[y1][x1] = MARKER

        if (y2 >= 0 and x2 >= 0)and (y2 <  NUM_ROWS and x2 < NUM_COLS):
            if copy_map[y2][x2] != MARKER:
                unique += 1
                copy_map[y2][x2] = MARKER



    print()
    print_map(copy_map, True)
    print("PART 1: ", unique)



def part2():
    f = open('../inputs/day8.txt')
    map = []
    antenna_list = []
    for line in f:
        map.append(list(line.strip()))

    NUM_COLS = len(map[0])
    NUM_ROWS = len(map)
    print(f"NUM ROWS: {NUM_ROWS} NUM_COLS: {NUM_COLS}")

    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if is_antenna(map[i][j]):
                antenna_list.append(Antenna(map[i][j], i, j))
    
    copy_map = deepcopy(map)

    track = []

    for i in range(len(antenna_list) - 1):
        a1 = antenna_list[i]
        for j in range(i+1, len(antenna_list)):
            a2 = antenna_list[j]
            if a1.id == a2.id:
                delta_y = (a2.y - a1.y) 
                delta_x = (a2.x - a1.x) 
                #m =(a2.y - a1.y) / (a2.x - a1.x) 
                track.append((a1, a2, delta_x, delta_y))
    print()


    unique = len(antenna_list)
    for (i, antenna_info) in enumerate(track):
        a1, a2, delta_x, delta_y = antenna_info


        y1 = a1.y - delta_y
        x1 = a1.x - delta_x
        condition1 = (y1 >= 0 and x1 >= 0) and (y1 < NUM_ROWS and x1 < NUM_COLS)
        while condition1:
            condition1 = (y1 >= 0 and x1 >= 0) and (y1 < NUM_ROWS and x1 < NUM_COLS)
            if condition1:
                if copy_map[y1][x1] != MARKER and copy_map[y1][x1] == '.': 
                    unique += 1
                    copy_map[y1][x1] = MARKER
            y1 -= delta_y
            x1 -= delta_x

        y2 = a2.y + delta_y
        x2 = a2.x + delta_x
        condition2 = (y2 >= 0 and x2 >= 0) and (y2 < NUM_ROWS and x2 < NUM_COLS)
        while condition2:
            condition2 = (y2 >= 0 and x2 >= 0) and (y2 < NUM_ROWS and x2 < NUM_COLS)
            #print(f"condition2: {condition} X: {x2} Y: {y2}")

            if  condition2:
                if copy_map[y2][x2] != MARKER and copy_map[y2][x2] == '.':
                    unique += 1
                    copy_map[y2][x2] = MARKER
            y2 += delta_y
            x2 += delta_x



    print()
    print_map(copy_map, True)
    print("PART 2: ", unique)

    test = 0
    for r in copy_map:
        for cell in r:
            if cell == '#':
                test += 1
    print(test+len(antenna_list))



#part1()
part2()
