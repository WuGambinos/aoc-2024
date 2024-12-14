from PIL import Image
from copy import deepcopy

f = open('../inputs/day14.txt')
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_str(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

class Robot:
    def __init__(self, p, v):
        self.p = Vector(p[0], p[1])
        self.v = Vector(v[0], v[1])

    def print(self):
        print(f"P: {self.p.as_str()} V: {self.v.as_str()}")
        

def print_grid(grid):
    for row in grid:
        print("".join(row))

#map_grid = [['.' for _ in range(11)] for _ in range(7)]
map_grid = [['.' for _ in range(101)] for _ in range(103)]

def safety_factor(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    MIDDLE_ROW = ROWS // 2
    MIDDLE_COL = COLS // 2
    q1 = 0 
    q2 = 0
    q3 = 0
    q4 = 0

    # Top Left Quadrant
    for i in range(0, MIDDLE_ROW):
        for j in range(0, MIDDLE_COL):
            if grid[i][j] != '.':
                q1 += int(grid[i][j])

    # Top Right Quadrant
    for i in range(0, MIDDLE_ROW):
        for j in range(MIDDLE_COL + 1, COLS):
            if grid[i][j] != '.':
                q2 += int(grid[i][j])

    # Bottom Left Quadrant
    for i in range(MIDDLE_ROW + 1, ROWS):
        for j in range(0, MIDDLE_COL):
            if grid[i][j] != '.':
                q3 += int(grid[i][j])

    # Bottom Right Quadrant
    for i in range(MIDDLE_ROW + 1, ROWS):
        for j in range(MIDDLE_COL + 1, COLS):
            if grid[i][j] != '.':
                q4 += int(grid[i][j])

    return q1 * q2 * q3 * q4


def move(robots, grid):

    for robot in robots:

        if grid[robot.p.y][robot.p.x] == '.':
            grid[robot.p.y][robot.p.x] = '1'
        elif grid[robot.p.y][robot.p.x] == '1':
            grid[robot.p.y][robot.p.x] = '.'
        else:
            grid[robot.p.y][robot.p.x] = str(int(grid[robot.p.y][robot.p.x]) - 1)

        new_x = robot.p.x + robot.v.x
        new_y = robot.p.y + robot.v.y

        if new_x < 0:
            adjust = new_x  - 0
            new_x = len(grid[0]) - abs(adjust)

        if new_y < 0:
            adjust = new_y - 0
            new_y = len(grid) - abs(adjust)

        if new_x >= len(grid[0]):
            adjust = new_x - len(grid[0])
            new_x = adjust


        if new_y >= len(grid):
            adjust = new_y - len(grid)
            new_y = adjust

        # Update position
        robot.p.x, robot.p.y = new_x, new_y

        p_x, p_y = robot.p.x, robot.p.y
        if grid[p_y][p_x] == '.':
            grid[p_y][p_x] = '1'
        else:
            grid[p_y][p_x] = str(int(grid[p_y][p_x]) + 1)

def create_image(grid, frame):
    MAX_X = 101
    MAX_Y = 103
    img = Image.new('1', (MAX_X, MAX_Y), 'black')
    pixels = img.load()


    for i in range(MAX_Y):
        for j in range(MAX_X):
            if grid[i][j] == '.':
                pixels[j, i] = 0
            else:
                pixels[j, i] = 1

    img.save(f"images/frame_{frame}.png")

def solve():

    robots = []
    for line in f:
        line = line.strip()
        p_info, v_info = line.split(" ")
        p_xy = p_info[2:] 
        v_xy = v_info[2:]

        p_x, p_y = p_xy.split(",")
        v_x, v_y = v_xy.split(",")

        p_x, p_y = int(p_x), int(p_y)
        v_x, v_y = int(v_x), int(v_y)


        r = Robot((p_x, p_y), (v_x, v_y))
        """
        r.print()
        print()
        """
        robots.append(r)

        if map_grid[p_y][p_x] == '.':
            map_grid[p_y][p_x] = '1'
        else:
            map_grid[p_y][p_x] = str(int(map_grid[p_y][p_x]) + 1)


    copy_map_grid = deepcopy(map_grid)

    seconds = 100
    for i in range(seconds):
        move(robots, map_grid)

    print("PART 1: ", safety_factor(map_grid))

    #Part 2
    seconds = 10000
    for i in range(seconds):
        print(f"ITERATION: {i}")
        move(robots, copy_map_grid)
        create_image(copy_map_grid, i)

solve()
