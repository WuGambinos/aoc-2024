from helper import read_file_to_string

input = read_file_to_string("../inputs/day3.txt")

""" 
REGEX 
import re
def day1(s):
    instructions = re.findall("mul\(\d+,\d+\)", s)
    first_num = ""
    second_num = ""
    res = 0
    for instruction in instructions:
        i = 0
        while i < (len(instruction)):
            ch = instruction[i]
            if ch == '(':
                i += 1
                while instruction[i].isdigit():
                    first_num += instruction[i]
                    i += 1
                
                i += 1

                while instruction[i].isdigit():
                    second_num += instruction[i]
                    i += 1

                i += 1
                res += int(first_num) * int(second_num)
                first_num = ""
                second_num = ""


            i += 1
    print("DAY 1:", res)

def day2(s):
    instructions = re.findall("(mul\(\d+,\d+\)|don't\(\)|do\(\))", s)
    first_num = ""
    second_num = ""
    res = 0
    enabled = True
    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        else:
            i = 0
            while i < (len(instruction)):
                ch = instruction[i]
                if ch == '(':
                    i += 1
                    while instruction[i].isdigit():
                        first_num += instruction[i]
                        i += 1
                    
                    i += 1

                    while instruction[i].isdigit():
                        second_num += instruction[i]
                        i += 1

                    i += 1
                    if enabled:
                        res += int(first_num) * int(second_num)
                    first_num = ""
                    second_num = ""


                i += 1
    print("DAY 2:", res)
"""

# CUSTOM
def parse_memory(s, part2):
    first_num = ""
    second_num = ""
    res = 0
    state = 0
    i = 0
    enabled = True

    while i < len(s):

        if (part2):
            if s[i:i+4] == "do()":
                enabled = True
            elif s[i:i+7] == "don't()":
                enabled = False

        if s[i:i+3] == "mul":
            state = 1
            #print("FIND MUL")
            i += 3
        elif state == 1 and s[i] == "(":
            state = 2
            #print("OPEN PAREN")
            i += 1

        elif state == 2 and s[i].isdigit():
            state = 3
            while(s[i].isdigit()):
                first_num += s[i]
                i+= 1
        elif state == 3 and s[i] == ",":
            state = 4
            #print("COMMA")
            i += 1
        
        elif state == 4 and s[i].isdigit():
            state = 5
            while(s[i].isdigit()):
                second_num += s[i]
                i+= 1

        elif state == 5 and s[i] == ")":
            #print("CLOSE PAREN")
            #print("VALID")
            #print()
            if first_num != "" and second_num != "" and enabled:
                string = f"mul({first_num},{second_num})"
                res += int(first_num) * int(second_num) 
            first_num = ""
            second_num = ""
            i += 1

        # Reset
        else:
            state = 0
            first_num = ""
            second_num = ""
            i += 1
    if part2:
        print("PART 2:", res)
    else:
        print("PART 1:", res)



# Part 1
parse_memory(input, False)
# Part 2
parse_memory(input, True)