from PIL import Image
import numpy as np

img = Image.new('RGB', (200, 100), color='black')
img.save('new_image.png')

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

def move(robot, grid, seconds, frame):
    for i in range(1, seconds+1):
        image_grid = np.array(grid_to_image_arr(map_grid))
        img_array = image_grid * 255
        img = Image.fromarray(img_array.astype(np.uint8))
        img.save("my_image" + str(frame[0]) + ".png")
        frame[0] += 1

        if grid[robot.p.y][robot.p.x] == '1':
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

def grid_to_image_arr(grid):

    result = []
    for row in grid:
        inner = []
        for c in row:
            if c =='.':
                inner.append(0)
            else:
                inner.append(1)

        result.append(inner)
    return result

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
        r.print()
        print()
        robots.append(r)

        if map_grid[p_y][p_x] == '.':
            map_grid[p_y][p_x] = '1'
        else:
            map_grid[p_y][p_x] = str(int(map_grid[p_y][p_x]) + 1)

    seconds = 100


    print("INITIAL STATE")
    print_grid(map_grid)
    print()



    """
    for r in robots:
        move(r, map_grid, seconds)
    """ 

    seconds = 2000
    frame = [0]
    for (i, r) in enumerate(robots):
        move(r, map_grid, seconds, frame)
        #print_grid(map_grid)
        #print()

    """
    image_grid = np.array(grid_to_image_arr(map_grid))
    for row in image_grid:
        print(row)

    img_array = image_grid * 255

    img = Image.fromarray(img_array.astype(np.uint8))

    img.save("my_image.png")
    """



    print("PART 1: ", safety_factor(map_grid))


solve()
