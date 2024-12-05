f = open('day1.txt', 'r')

def day1():
    left_list = [] 
    right_list = []

    for line in f:
        nums = line.split()
        left_list.append(int(nums[0]))
        right_list.append(int(nums[1]))

    left_list.sort()
    right_list.sort()

    sum = 0
    for i in range(len(left_list)):
        dist = abs(left_list[i] - right_list[i])
        sum += dist

    print(sum)

def day2():
    left_list = [] 
    right_list = []

    for line in f:
        nums = line.split()
        left_list.append(int(nums[0]))
        right_list.append(int(nums[1]))

    total = 0
    for left_num  in left_list:
        for right_num in right_list:
            if left_num == right_num:
                total += left_num

    print(total)

day2()
