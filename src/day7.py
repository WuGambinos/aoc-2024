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
        pass
        

    def recurse(self, nums, idx, accum, found, operator, target_value):
        if (idx == len(nums)):
            return found

        res_found = False
        for i in range(idx+1, len(nums)+1):
            if operator == "*":
                accum1 = accum * nums[idx]
                new_found = (accum1 == target_value) or found

                # Attempt Multplication Next
                res_found = res_found or self.recurse(nums, i, accum1, new_found, '*', target_value) 

                # Attempt Addition Next
                res_found = res_found or self.recurse(nums, i, accum1, new_found, '+', target_value)
            else:
                accum2 = accum + nums[idx]
                new_found = (accum2 == target_value) or found

                # Attempt Multplication Next
                res_found = res_found or self.recurse(nums, i, accum2, new_found, '*', target_value)

                # Attempt Addition Next
                res_found = res_found or self.recurse(nums, i, accum2, new_found, '+', target_value)

        return res_found

    def part1(self):
        lines = read_file_to_list("../inputs/day7.txt")
        m = {}

        # Parse data
        for line in lines:
            data = line.split(":")
            target_val = int(data[0])
            nums = data[1].strip().split(" ")
            nums = [int(n) for n in nums]
            if target_val not in m:
                m[target_val] = [nums]
            else: 
                m[target_val].append(nums)
        
        total = 0
        line_num = 1

        for (k, v) in m.items():
            for lst in v:
                t1 = s.recurse(lst, 1, lst[0], False, '*', k)
                t2 = s.recurse(lst, 1, lst[0], False, '+', k)

                # Valid 
                if t1 or t2:
                    print("VALID LINE NUM", line_num)
                    total += k
                else:
                    print("INVALID LINE NUM", line_num)

            line_num  += len(v)
        print("PART 1", total)


s = Solution() 
s.part1()
