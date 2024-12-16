from os import walk


f = open('../inputs/day15_test2.txt', 'r')


class Boxes: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def print(self):
        print(f"BOX: x: {self.x} y: {self.y}")

def print_map(map):
    for row in map:
        print("".join(row))





def recurse_move(map, directions, idx, robot_x, robot_y, visited):

    if idx == len(directions):
        return

    print(f"ATTEMPT\tROBOT X: {robot_x} Y: {robot_y} CELL: {map[robot_y][robot_x]}")
    if map[robot_y][robot_x] == "#":
        dir = directions[idx]
        x = dir[1][0]
        y = dir[1][1]
        return recurse_move(map, directions, idx+1, robot_x +  x, robot_y + y, visited)

    if (robot_y, robot_x) in visited:
        return 

    visited.append((robot_y, robot_x))
    print(f"VALID\tROBOT X: {robot_x} Y: {robot_y}")
    print()

    x = directions[idx][1][0]
    y = directions[idx][1][1]

    return recurse_move(map, directions, idx+1, robot_x + x, robot_y + y, visited)



"""
def move(map, directions, robot_x, robot_y):
    LEFT    = ("<", -1)
    RIGHT   = (">", 1)
    UP      = ("^", -1)
    DOWN    = ("v", 1)
    BOX = "O"
    WALL = "#"
    ROBOT = "@"
    EMPTY = "."
    print("ROBOT")

    for i in range(4):
        dir = directions[i]
        if dir == LEFT[0]:
            # Box in Way
            next_x = robot_x + LEFT[1]
            next_y = robot_y
            print("LEFT: ", i)
            if map[next_y][next_x] == BOX:
                print("BOX")
                next_next_x, next_next_y = next_x + LEFT[1], next_y

                # Move Box
                map[robot_y][robot_x] = EMPTY
                map[next_y][next_x] = ROBOT
                map[next_next_y][next_next_x] = BOX

            elif map[next_y][next_x] == WALL:
                print("WALL")
            # Empty
            else:
                print("EMPTY")


        elif dir == RIGHT[0]:
            print("RIGHT: ", i)
        elif dir == UP[0]:
            print("UP: ", i)
            # Box in Way
            next_x = robot_x
            next_y = robot_y + UP[1]
            if map[next_y][next_x] == BOX:
                print("BOX")
                next_next_x, next_next_y = next_x , next_y + UP[1]

                # Move Box
                map[robot_y][robot_x] = EMPTY
                map[next_y][next_x] = ROBOT
                map[next_next_y][next_next_x] = BOX

            elif map[next_y][next_x] == WALL:
                print("WALL")

            # Empty
            else:
                print("EMPTY")
                map[robot_y][robot_x] = EMPTY
                map[next_y][next_x] = ROBOT
        elif dir == DOWN[0]:
            print("DOWN: ", i)

        print_map(map)
        print()
"""


LEFT    = ("<", (-1, 0))
RIGHT   = (">", (1, 0))
UP      = ("^", (0, -1))
DOWN    = ("v", (0, 1))
def directions_str_to_lst(directions):
    result = []
    for ch in directions:
        if ch == "<":
            result.append(LEFT)
        elif ch == ">":
            result.append(RIGHT)
        elif ch == "^":
            result.append(UP)
        elif ch == "v":
            result.append(DOWN)

    return result


def solve():
    warehouse_map   = []
    directions_str      = []
    boxes           = []

    switch = False
    for line in f:
        line = line.strip()
        if not line:
            switch = True
        else:
            if switch:
                directions_str = line
            else:
                warehouse_map.append(list(line))

    robot_x, robot_y = None, None

    for (i, row) in enumerate(warehouse_map):
        for (j, cell) in enumerate(row):
            if cell == '@':
                robot_y, robot_x = i, j
            elif cell == 'O':
                boxes.append(Boxes(j, i))

    
    directions = directions_str_to_lst(directions_str)

    print(f" X: {robot_x} Y: {robot_y}")

    for row in directions:
        print(row)

    #move(warehouse_map, directions, robot_x, robot_y)
    recurse_move(warehouse_map, directions, 0, robot_x, robot_y, [])

solve()

