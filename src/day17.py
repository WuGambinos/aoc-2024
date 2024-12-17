#from enum import Enum

REGISTER_A = 4
REGISTER_B = 5 
REGISTER_C = 6
I_ADV = 0
I_BXL = 1
I_BST = 2
I_JNZ = 3
I_BXC = 4
I_OUT = 5
I_BDV = 6
I_CDV = 7

"""
class Registers(Enum):
    A = 4
    B = 5 
    C = 6

class Instructions(Enum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7
    pass
"""

def combo_operand(operand):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return REGISTER_A
    elif operand == 5:
        return REGISTER_B
    elif operand == 6:
        return REGISTER_C

"""
def combo_operand(operand):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return Registers.A.value
    elif operand == 5:
        return Registers.B.value
    elif operand == 6:
        return Registers.C.value

def run_program(program, registers):
    pc = 0
    output = []
        
    while pc < len(program):
        instr = program[pc]
        operand = program[pc+1]
        combo_op =  combo_operand(program[pc+1])
        combo_op = combo_op if combo_op < 4 else registers[combo_op]

        #print(f"INSTRUCTION: {instr} OPERAND: {operand}")
        
        jmp = False

        match instr:
            case Instructions.ADV.value:
                res = registers[Registers.A.value] // (2 ** combo_op)
                registers[Registers.A.value] = res
                #print("A: ", registers[Registers.A.value])

            case Instructions.BXL.value:
                res = registers[Registers.B.value] ^ (operand)
                registers[Registers.B.value] = res
                #print("B: ", registers[Registers.A.value])

            case Instructions.BST.value:
                res = combo_op % 8
                registers[Registers.B.value] = res

            case Instructions.JNZ.value:
                if registers[Registers.A.value] != 0:
                    jmp = True
                    pc = operand

            case Instructions.BXC.value:
                registers[Registers.B.value] = registers[Registers.B.value] ^ registers[Registers.C.value]

            case Instructions.OUT.value:
                output.append(combo_op % 8)

            case Instructions.BDV.value:
                res = registers[Registers.A.value] // (2 ** combo_op)
                registers[Registers.B.value] = res

            case Instructions.CDV.value:
                res = registers[Registers.A.value] // (2 ** combo_op)
                registers[Registers.C.value] = res

            case _:
                print("REACHED WILDCARD")
                pass

        if not jmp:
            pc += 2
        print(registers)
        print("OUTPUT:", output)
    """

#START = 5000000
START = 0
def find_program(program, registers):

    i = START
    while i < 10:
        registers[REGISTER_A] = i
        pc = 0
        output = []
        #print("ITERATION: ", i)
        
        while pc < len(program):
            instr = program[pc]
            operand = program[pc+1]
            combo_op =  combo_operand(program[pc+1])
            combo_op = combo_op if combo_op < 4 else registers[combo_op]

            #print(f"INSTRUCTION: {instr} OPERAND: {operand}")
            
            jmp = False
            #print("INSTRUCTION" , instr, "OPERAND:",operand)
            if instr == I_ADV:
                res = registers[REGISTER_A] // (2 ** combo_op)
                registers[REGISTER_A] = res
                #print("ADV: A // ", 2 ** combo_op)

            elif instr == I_BXL:
                res = registers[REGISTER_B] ^ (operand)
                registers[REGISTER_B] = res
                #print("B ^= ", operand, "=", res)

            elif instr == I_BST:
                res = combo_op % 8
                registers[REGISTER_B] = res
                #print("BST: ", combo_op, "%", "8")

            elif instr == I_JNZ:
                if registers[REGISTER_A] != 0:
                    jmp = True
                    pc = operand

            elif instr == I_BXC:
                registers[REGISTER_B] = registers[REGISTER_B] ^ registers[REGISTER_C]
                """
                print(registers[REGISTER_B], registers[REGISTER_C])
                print("BXC B" ,"= B ^ C")
                print()
                """

            elif instr == I_OUT:
                #print("B, ", registers[REGISTER_B])
                output.append(combo_op % 8)

            elif instr == I_BDV:
                res = registers[REGISTER_A] // (2 ** combo_op)
                registers[REGISTER_B] = res

            elif instr == I_CDV:
                res = registers[REGISTER_A] // (2 ** combo_op)
                registers[REGISTER_C] = res
                #print("CDV: A // ", 2 ** combo_op)

            else:
                print("REACHED WILDCARD")
                pass

            if not jmp:
                pc += 2

            if output == program:
                print(i)
                return

            if len(output) > len(program):
                break
            #print(registers)
        print("OUTPUT:", output)
        print()
        i += 1


def solve(part1):
    registers = {}
    program = None

    f = open('../inputs/day17.txt')
    switch = False
    reg = 4
    for line in f:
        line = line.strip()
        if not line:
            switch = True
            pass
        else:
            if switch:
                program_info = line.split(":")
                temp = program_info[1].split(",")
                program = [int(n) for n in temp]
            else:
                reg_info = line.split(":")
                registers[reg] = (int(reg_info[1]))
                reg += 1

    for (r, v) in registers.items():
        print(r, v)

    print()
    print(program)

    if part1:
        run_program(program,registers)
    else:
        find_program(program,registers)


#solve(True)
solve(False)
