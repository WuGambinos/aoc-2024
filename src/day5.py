from helper import read_file_to_list

lines = read_file_to_list("../inputs/day5.txt")

valid_updates = []
ordering = [] 
updates = []
m = {}

class PageOrder:
    def __init__(self, before, after):
        self.before = before 
        self.after = after


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
            lst = [after]
            m[before] = lst
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
    nums = update.split(",")
    nums = [int(n) for n in nums]

    for i in range(len(nums)):
        if nums[i] not in m and i == len(nums) - 1:
            return True

        elif nums[i] not in m:
            return check(nums, nums[i])

        order_list = m[nums[i]]
        for j in range(i+1, len(nums)):
            if nums[j] not in order_list:
                return False
    return True


def solve():
    for update in updates:
        valid = valid_page_update(update)
        print(update, valid)
        if (valid):
            valid_updates.append(update)
    print(valid_updates)

    nums_2d = []
    for valid in valid_updates:
        nums = valid.split(",")
        nums = [int(n) for n in nums]
        nums_2d.append(nums)

    res = 0
    for valid in nums_2d:
        if len(valid) % 2 == 0 :
            res += valid[len(valid) // 2 - 1]
        else:
            res += valid[len(valid) // 2]

    print("DAY 1: ", res)

setup()
solve()