from helper import read_file_to_string
import sympy as sp







f = open('../inputs/day13.txt', 'r')


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

"""
def recurse(acc,  n1, n2, visited, count_n1, count_n2):

    if acc == 0:
        return count_n1, count_n2

    if acc  < 0:
        return None

    if acc in visited:
        return None

    visited.add(acc)

    result_n1 = recurse(acc - n1, n1, n2, visited, count_n1+1, count_n2)
    if result_n1:
        return result_n1


    result_n2 = recurse(acc - n2, n1, n2, visited, count_n1, count_n2+1)
    if result_n2:
        return result_n2

    visited.remove(acc)

    return None
"""


def solve():
    turns = []
    inner = []

    buttons = []
    claw_machines = {}

    A_TOKEN_COST = 3
    B_TOKEN_COST = 1

    for line in f:
        if not line.strip() :
            print("EMPTY")
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
        p.print()
        b1, b2 = buttons[0], buttons[1]
        x1, x2 = b1.dx, b2.dx
        y1, y2 = b1.dy, b2.dy

        eq1 = x1 * x + x2 * y - p.x
        eq2 = y1 * x + y2 * y - p.y

        solution = sp.solve((eq1, eq2), (x, y))
        total_x = solution[x]
        total_y = solution[y]
        if type(total_x) == sp.core.numbers.Integer and type(total_y) == sp.core.numbers.Integer:
            cost = total_x * A_TOKEN_COST + B_TOKEN_COST * total_y
            total_cost += cost
            """
            print(total_x, total_y)
            print("COST", cost)
            print()
            """

    print("PART 1", total_cost)
    

solve()


