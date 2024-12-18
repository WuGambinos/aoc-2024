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


def combo_operand(operand):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return REGISTER_A
    elif operand == 5:
        return REGISTER_B
    elif operand == 6:
        return REGISTER_C


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


    return output

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

    if part1:
        print("PART 1", run_program(program,registers))
    else:
        candidates = [0]
        for l in range(len(program)):
            next_candidates = []
            for val in candidates:
                for i in range(8):
                    target = (val << 3) + i
                    registers[REGISTER_A] = target
                    res =  run_program(program, registers)

                    if res == program[-l-1:]:
                        next_candidates.append(target)

            candidates = next_candidates

        print("PART 2: ", min(candidates))

solve(True)
solve(False)
