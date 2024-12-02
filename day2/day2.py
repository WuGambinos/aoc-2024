import copy
f = open("day2.txt", "r")
lines = []
for line in f:
    line = line.strip()
    print(line)
    line = line.split()
    lines.append(line)


def check_strict_order(lst):
    if all(lst[i] < lst[i + 1] and ((lst[i+1] - lst[i]) <= 3 and (lst[i+1] - lst[i]) >= 1) for i in range(len(lst) - 1)):
        return True
    elif all(lst[i] > lst[i + 1] and (lst[i] - lst[i+1] <= 3 and (lst[i] - lst[i+1] >= 1)) for i in range(len(lst) - 1)):
        return True
    else:
        return False

def day1():
    grid = [[int(num) for num in row] for row in lines]

    answer = 0
    for row in grid:
        result = check_strict_order(row)
        print(row, result)
        if result:
            answer += 1

    print(answer)


def day2():
    grid = [[int(num) for num in row] for row in lines]

    answer = 0
    skip = False
    for row in grid:
        result = check_strict_order(row)
        print(row, result)
        if result:
            answer += 1
        else:
            skip = False
            for i in range(len(row)):
                copy_arr = copy.deepcopy(row)
                copy_arr.pop(i)
                if check_strict_order(copy_arr) and not skip:
                    skip = True
                    answer += 1

            print()

    print(answer)

day2()