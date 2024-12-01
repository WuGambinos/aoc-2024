f = open('day1.txt', 'r')
lst1 = [] 
lst2 = []

def day1():
    for line in f:
        nums = line.split()
        lst1.append(int(nums[0]))
        lst2.append(int(nums[1]))

    lst1.sort()
    lst2.sort()
    sum = 0
    for i in range(len(lst1)):
        dist = abs(lst1[i] - lst2[i])
        sum += dist

    print(sum)

def day2():
    left_list = [] 
    right_list = []
    map = {}
    for line in f:
        nums = line.split()
        left_list.append(int(nums[0]))
        right_list.append(int(nums[1]))


    for left_num  in left_list:
        count = 0 
        for right_num in right_list:
            if left_num == right_num:
                count += 1

        map[left_num] = count

    total = 0 
    for left_num in left_list:
        total += map[left_num] * left_num

    print(total)

day2()
