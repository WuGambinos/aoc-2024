import re
f = open('../inputs/day19.txt')

towels = []
designs = []

for (i,line) in enumerate(f):
    line = line.strip()
    if i == 0:
        towels = line.split(",")
        towels = [s.strip() for s in towels]
    elif line:
        designs.append(line)



def num_ways(design, memo):

    # Num ways has already been calculated for this design str
    if design in memo:
        return memo[design]

    # Valid Possiblity
    if not design:
        return 1

    count = 0
    for tow in towels:
        if design.startswith(tow):
            match = re.search(tow, design)
            res = num_ways(design[match.end():], memo)
            count += res

    # Save num ways for this design str
    memo[design] = count

    return count

    

def solve(part1):
    possible = 0
    different_ways = 0

    for (_i, d) in enumerate(designs):
        memo = {}
        if part1:
            res = num_ways(d, memo)
            if res != 0:
                possible += 1
        else:
            different_ways += num_ways(d ,memo)


    if part1:
        print("PART 1", possible)
    else:
        print("PART 2", different_ways)

solve(True)
solve(False)
