from helper import read_file_to_list
from functools import cmp_to_key

lines = read_file_to_list("../inputs/day5.txt")

ordering = [] 
updates = []
m = {}

def setup():
    empty_line_seen = False
    for line in lines:
        if empty_line_seen:
            updates.append(line)
        elif line:
            ordering.append(line)

        if not line:
            empty_line_seen = True

    # Setup Map
    for order in ordering:
        data = order.split("|")
        before = int(data[0])
        after = int(data[1])
        if (before not in m):
            temp_list = [after]
            m[before] = temp_list
        else:
            m[before].append(after)

def check(update, value):
    for (k, value_list) in m.items():
        for v in value_list:
            if (v == value):
                if k in update:
                    return False
    return True

def valid_page_update(update):

    for i in range(len(update)):
        if update[i] not in m and i == len(update) - 1:
            return True

        elif update[i] not in m:
            return check(update, update[i])

        order_list = m[update[i]]
        for j in range(i+1, len(update)):
            if update[j] not in order_list:
                return False
    return True


def sum_middle(updates):
    res = 0
    for update in updates:
        if len(update) % 2 == 0 :
            res += update[len(update) // 2 - 1]
        else:
            res += update[len(update) // 2]
    return res

def custom_cmp(x, y):
    if x in m:
        order_list = m[x]
        if y in order_list:
            return -1
        else:
            return 1
    else:
        return 1

def fix_order(invalid_updates):
    cmp_key  = cmp_to_key(custom_cmp)
    for invalid in invalid_updates:
        invalid.sort(key=cmp_key)


def solve():
    valid_updates = []
    invalid_updates = []

    for update in updates:
        nums = update.split(",")
        nums = [int(n) for n in nums]
        valid = valid_page_update(nums)
        if (valid):
            valid_updates.append(nums)
        else:
            invalid_updates.append(nums)

    day1 = sum_middle(valid_updates)

    fix_order(invalid_updates)
    day2 = sum_middle(invalid_updates)  

    print("PART 1: ", day1)
    print("PART 2: ", day2)

setup()
solve()