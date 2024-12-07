from helper import read_file_to_list

def do_operation(x, y, op):
    if op == "*":
        return x * y
    elif op == "+":
        return x + y
    else:
        raise Exception("NOT VALID OPERATOR")

class Solution():
    def __init__(self):
        self.s1 = ""
        self.s2 = ""
        self.sum_track = []

    """
    def custom_recurse(self, nums, idx, acc, found, operator, target_value):

        if (idx == len(nums)):
            return found

        for i in range(idx+1, len(nums)+1):
            if operator == "*":
                acc1 = acc * nums[idx]
                print(f"ACC: {acc1} TARGET_VALUE: {target_value}")
                self.sum_track.append(acc1 == target_value)
                if i < len(nums):
                    self.s1 += str(acc) + operator + str(nums[i])
                    self.s2 += str(acc) + operator + str(nums[i])

                self.custom_recurse(nums, i, acc1, '*', target_value) 
                self.custom_recurse(nums, i, acc1, '+', target_value)
                self.sum_track.extend(self.custom_recurse(nums, i, acc1, '*', target_value))
                self.sum_track.extend(self.custom_recurse(nums, i, acc1, '+', target_value))
            else:
                acc2 = acc  + nums[idx]
                print(f"ACC: {acc2} TARGET_VALUE: {target_value}")
                self.sum_track.append(acc2 == target_value)
                if i < len(nums):
                    self.s1 += str(acc) + operator + str(nums[i])
                    self.s2 += str(acc) + operator + str(nums[i])
                self.custom_recurse(nums, i, acc2, '*', target_value)
                self.custom_recurse(nums, i, acc2, '+', target_value)
                sum_track.extend(self.custom_recurse(nums, i, acc2, '*', target_value))

        return self.sum_track
    """

    def custom_recurse(self, nums, idx, acc, found, operator, target_value):

        if (idx == len(nums)):
            return found


        res_found = False
        for i in range(idx+1, len(nums)+1):
            if operator == "*":
                acc1 = acc * nums[idx]
                new_found = (acc1 == target_value) or found
                """
                if i < len(nums):
                    self.s1 += str(acc) + operator + str(nums[i])
                    self.s2 += str(acc) + operator + str(nums[i])
                """
                res_found = res_found or self.custom_recurse(nums, i, acc1, new_found, '*', target_value) 
                res_found = res_found or self.custom_recurse(nums, i, acc1, new_found, '+', target_value)
            else:
                acc2 = acc  + nums[idx]
                new_found = (acc2 == target_value) or found

                """
                if i < len(nums):
                    self.s1 += str(acc) + operator + str(nums[i])
                    self.s2 += str(acc) + operator + str(nums[i])
                """
                res_found = res_found or self.custom_recurse(nums, i, acc2, new_found, '*', target_value)
                res_found = res_found or self.custom_recurse(nums, i, acc2, new_found, '+', target_value)

        return res_found


def day1():
    s = Solution()
    lines = read_file_to_list("../inputs/day7.txt")
    m = {}
    for line in lines:
        data = line.split(":")
        target_val = int(data[0])
        nums = data[1].strip().split(" ")
        nums = [int(n) for n in nums]
        if target_val not in m:
            m[target_val] = nums

    total = 0
    line_num = 0 
    valid_count = 0
    for (k, v) in m.items():

        """
        t1 = set(s.custom_recurse(v, 1, v[0], '*', k))
        t2 = set(s.custom_recurse(v, 1, v[0], '+', k))
        """
        t1 = s.custom_recurse(v, 1, v[0], False, '*', k)
        t2 = s.custom_recurse(v, 1, v[0], False, '+', k)

        """
        print(s.s1)
        print()
        print(s.s2)
        s.s1 = ""
        s.s2 = ""
        """
        """
        print("T1", t1)
        print("T2", t2)
        print()
        """
        if t1 or t2:
            total += k

        print("LINE NUM", line_num)
        line_num  += 1




    print()
    print("VALID COUNT: ", valid_count)
    print(total)
    print()


    
day1()
