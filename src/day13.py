from helper import read_file_to_string
import sympy as sp

CONVERSION = 10000000000000
A_TOKEN_COST = 3
B_TOKEN_COST = 1


class Prize:
    def __init__(self,  x, y):
        self.x = x
        self.y = y

    def print(self):
        print(f"X: {self.x} Y: {self.y}")

class Button:
    def __init__(self,  label, dx, dy):
        self.label = label
        self.dx = dx
        self.dy = dy

    def print(self):
        print(f"LABEL {self.label} X: {self.dx} Y: {self.dy}")

def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm


# Solve System of Equation
def elimination(x1, y1, t1, x2, y2, t2):
    lcm = compute_lcm(x1, x2)
    m1 = lcm // x1
    m2 = lcm // x2

    adjusted_y1 = y1
    adjusted_y2 = y2

    adjusted_y1 *= m1
    adjusted_y2 *= m2

    adjusted_t1 = t1
    adjusted_t2 = t2

    adjusted_t1 *= m1
    adjusted_t2 *= m2

    new_y = adjusted_y2 - adjusted_y1
    adjusted_t = adjusted_t2 - adjusted_t1

    if adjusted_t % new_y != 0:
        return None

    final_y = adjusted_t // new_y


    if (t1 - (y1 * final_y)) % x1 != 0:
        return None

    final_x = (t1 - (y1 * final_y)) // x1

    return (final_x, final_y)

def solve(part2):
    turns = []
    inner = []

    buttons = []
    claw_machines = {}


    f = open('../inputs/day13.txt', 'r')
    for line in f:
        if not line.strip() :
            turns.append(inner)
            inner = []
        else:
            inner.append(line.strip())

    turns.append(inner)

    for turn in turns:

        for info in turn:
            if info[0] == 'B':
                label = info.split(":")[0].split(" ")[1]
                button_x, button_y = info.split(":")[1].split(",")
                x = button_x.split("+")[1]
                y = button_y.split("+")[1]
                buttons.append(Button(label, int(x), int(y)))

            elif info[0] == 'P':
                prize_x, prize_y = info.split(":")[1].split(",")
                x = prize_x.split("=")[1]
                y = prize_y.split("=")[1]
                prize = Prize(int(x), int(y))
                claw_machines[prize] = buttons
                buttons = []

    print()

    x, y = sp.symbols('x y')
    total_cost = 0

    for (p, buttons) in claw_machines.items():
        b1, b2 = buttons[0], buttons[1]
        x1, x2 = b1.dx, b2.dx
        y1, y2 = b1.dy, b2.dy

        if part2:
            p.x += CONVERSION
            p.y += CONVERSION

        res = elimination(x1, x2, p.x,  y1, y2, p.y)
        if res != None:
            total_x, total_y = res[0], res[1]
            cost = total_x * A_TOKEN_COST + B_TOKEN_COST * total_y
            total_cost += cost

        """
        eq1 = x1 * x + x2 * y - p.x
        eq2 = y1 * x + y2 * y - p.y

        solution = sp.solve((eq1, eq2), (x, y))
        total_x = solution[x]
        total_y = solution[y]
        if type(total_x) == sp.core.numbers.Integer and type(total_y) == sp.core.numbers.Integer:
            cost = total_x * A_TOKEN_COST + B_TOKEN_COST * total_y
            total_cost += cost
        """

    if part2:
        print("PART 2", total_cost)
    else:
        print("PART 1", total_cost)

solve(False)
solve(True)



