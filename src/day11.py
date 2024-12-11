import functools

@functools.cache
def recurse(n, depth, max_depth):

        if depth == max_depth:
            return 1
        
        depth += 1

        if n == 0:
            return recurse(1, depth, max_depth)

        else:

            s = str(n)
            l = len(s)
            if l % 2 == 0:
                return recurse(int(s[:l//2]), depth, max_depth) + recurse(int(s[l//2:]), depth, max_depth)

            else:
                return recurse(n * 2024, depth, max_depth)

def solve():
    f = open('../inputs/day11.txt')
    stones = f.readline().strip().split(" ")
    stones = [int(n) for n in stones]

    print("STONES", stones)
    part1 = sum([recurse(n, 0, 25) for n in stones ])
    print("PART 1", part1)

    part2 = sum([recurse(n, 0, 75) for n in stones ])
    print("PART 2", part2)


solve()
