f = open('../inputs/day24.txt', 'r')


OPERATIONS = ["AND", "XOR", "OR"]

class Wire:
    def __init__(self, ident, value):
        self.ident = ident
        self.value = value

    def print(self):
        print("IDENT: ", self.ident, "VALUE: ", self.value)

class Gate:
    def __init__(self, left, right, op, result):
        self.left = left
        self.right = right
        self.op = op
        self.result = result

    def do_operation(self, wire_map):
        try:
            if self.op == "AND":
                wire_map[self.result] = wire_map[self.left] & wire_map[self.right]
            elif self.op == "XOR":
                wire_map[self.result] = wire_map[self.left] ^ wire_map[self.right]
            elif self.op == "OR":
                wire_map[self.result] = wire_map[self.left] | wire_map[self.right]
            return True

        except KeyError:
            return False


    def print(self):
        print("LEFT: ", self.left, "OP: ", self.op, "RIGHT: ", self.right, "RESULT: ", self.result)



def solve():

    switch = False
    gate_infos = []
    gates =[]

    wire_infos = []
    wire_map = {}
    init_wires= []

    for line in f:
        line = line.strip()
        if line:
            if switch:
                gate_infos.append(line)
            else:
                wire_infos.append(line)

        else:
            switch = True

    for wire in wire_infos:
        wire_name, value = wire.split(":")
        value = int(value.strip())
        wire_map[wire_name] = value
        init_wires.append((wire_name, value))

    for g in gate_infos:
        left, result_wire = g.split ("->")
        left, result_wire = left.strip(), result_wire.strip()
        s = ""
        for op in OPERATIONS:
            if left.find(op) != -1:
                s = op
                break

        left_wire, right_wire = left.split(s)
        left_wire, right_wire = left_wire.strip(), right_wire.strip()

        gates.append(Gate(left_wire, right_wire, s, result_wire))

    def recurse(gates, operand):
        for g in gates:
            if g.result == operand:
                if g.do_operation(wire_map):
                    return True
                else:
                    recurse(gates, g.left)
                    recurse(gates, g.right)
            g.do_operation(wire_map)


    for (i, g) in enumerate(gates):
        if g.result[0] != "z":
            if g.left not in wire_map:
                recurse(gates, g.left)

            if g.right not in wire_map:
                recurse(gates, g.right)

            if g.right in wire_map and g.left in wire_map:
                g.do_operation(wire_map)

    i = 0 
    for g in gates:
        if g.result[0] == "z":
            if g.left not in wire_map:
                recurse(gates, g.left)

            if g.right not in wire_map:
                recurse(gates, g.right)

            if g.right in wire_map and g.left in wire_map:
                g.do_operation(wire_map)

            i += 1


    z_wires = []
    bin_num = ""
    for (w, v) in wire_map.items():
        if w[0] == "z":
            z_wires.append((w, v))

    z_wires.sort(reverse=True)

    for b in z_wires:
        bin_num += str(b[1])

    print("PART 1")
    print("BITS", len(bin_num))
    print(bin_num)
    print("ANSWER", int(bin_num, 2))
    print()

    # PART 2
    print("PART 2")
    init_wires.sort()
    x = ""
    y = ""
    
    for wire  in init_wires:
        (name, value) = wire
        if name[0] == "x":
            x += str(value)
        elif name[0] == "y":
            y += str(value)

    x = x[::-1]
    y = y[::-1]
    print(f"X:\t\t 0b{x}")
    print(f"Y:\t\t 0b{y} ")

    print()
    print(f"WRONG Z:\t0b{bin_num}")
    print(f"CORRECT Z:\t{bin(int(x, 2)  + int(y, 2))}")
    print(f"ACTUAL Z:\t{int(x, 2)  + int(y, 2)}")

    correct_z = bin(int(x, 2) + int(y, 2))[::-1]
    wrong_z = bin_num[::-1]

    for i in range(len(correct_z)):
        if correct_z[i] != wrong_z[i]:
            print("I: ", i)
            break


solve()
