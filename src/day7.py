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
        self.p2 = False
        

    def recurse(self, nums, idx, accum, found, operator, target_value):
        if (idx == len(nums)):
            return found

        res_found = False
        for i in range(idx+1, len(nums)+1):
            if operator == "*":
                accum1 = accum * nums[idx]
                #print("ACCUM 1", accum1)
                new_found = (accum1 == target_value) or found

                # Attempt Multplication Next
                res_found = res_found or self.recurse(nums, i, accum1, new_found, '*', target_value) 

                # Attempt Addition Next
                res_found = res_found or self.recurse(nums, i, accum1, new_found, '+', target_value)

                if self.p2:
                # Attempt Combination Next
                    res_found = res_found or self.recurse(nums, i, accum1, new_found, '||', target_value)

            elif operator == "+":
                accum2 = accum + nums[idx]
                #print("ACCUM 2", accum2)
                new_found = (accum2 == target_value) or found

                # Attempt Multplication Next
                res_found = res_found or self.recurse(nums, i, accum2, new_found, '*', target_value)

                # Attempt Addition Next
                res_found = res_found or self.recurse(nums, i, accum2, new_found, '+', target_value)

                if self.p2:
                    # Attempt Combination Next
                    res_found = res_found or self.recurse(nums, i, accum2, new_found, '||', target_value)
            elif operator == "||":
                accum3 = int(str(accum) + str(nums[idx]))
                #print("ACCUM 3", accum3)
                new_found = (accum3 == target_value) or found

                # Attempt Multplication Next
                res_found = res_found or self.recurse(nums, i, accum3, new_found, '*', target_value)

                # Attempt Addition Next
                res_found = res_found or self.recurse(nums, i, accum3, new_found, '+', target_value)

                if self.p2:
                    # Attempt Combination Next
                    res_found = res_found or self.recurse(nums, i, accum3, new_found, '||', target_value)


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
                    #print("VALID LINE NUM", line_num)
                    total += k
                else:
                    #print("INVALID LINE NUM", line_num)
                    pass

            line_num  += len(v)
        print("PART 1", total)
        return total

    def part2(self):
        valid = 0
        self.p2 = True
        lines = read_file_to_list("../inputs/day7.txt")
        m = {}

        total = 0
        line_num = 1
        # Parse data
        for line in lines:
            data = line.split(":")
            target_value = int(data[0])
            nums = data[1].strip().split(" ")
            nums = [int(n) for n in nums]
            t1 = s.recurse(nums, 1, nums[0], False, '*', target_value)
            t2 = s.recurse(nums, 1, nums[0], False, '+', target_value)
            t3 = s.recurse(nums, 1, nums[0], False, '||', target_value)
            if t1 or t2 or t3:
                print("VALID LINE NUM", line_num-1, target_value, nums)
                valid += 1
                total += target_value
            line_num += 1
            """
            if target_val not in m:
                m[target_val] = [nums]
            else: 
                m[target_val].append(nums)
            """
        
        """
        total = 0
        line_num = 1

        for (k, v) in m.items():
            for lst in v:
                t1 = s.recurse(lst, 1, lst[0], False, '*', k)
                t2 = s.recurse(lst, 1, lst[0], False, '+', k)
                t3 = s.recurse(lst, 1, lst[0], False, '||', k)

                # Valid 
                if t1 or t2 or t3:
                    print("VALID LINE NUM", line_num-1, k, lst)
                    valid += 1
                    total += k
            
            line_num  += len(v)
        """
        print(total)
        print("PART 2: ", total)
        print("VALID", valid)


s = Solution() 
#s.part1()
s.part2()
