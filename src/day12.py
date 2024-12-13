from helper import read_file_to_list


map = read_file_to_list('../inputs/day12.txt')
perimeters = {}


def find_perimeter_and_area(garden, label,  r, c, visited):

    if (r >= len(garden) or r < 0): 
        #print(f"BORDER: R: {r} C: {c}")
        return (0, 1)

    if (c >= len(garden[0]) or c < 0): 
        #print(f"BORDER: R: {r} C: {c}")
        return (0, 1)

    if garden[r][c] != label:
        #print(f"NOT LABEL: R: {r} C: {c}")
        return (0, 1)

    if (r, c) in visited:
        return (0, 0)

    visited.append((r, c))


    area = 1 
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0,1)]

    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc


        if new_r < 0 or new_r >= len(garden) or new_c < 0 or new_c >= len(garden[0]):
            perimeter += 1

        else:
            a, p =  find_perimeter_and_area(garden, label,  new_r, new_c, visited)
            area += a 
            perimeter += p

    return area, perimeter

def find_num_sides(garden, label, r, c,  visited):
    if r >= len(garden) or r < 0 or c >= len(garden[0]) or c < 0: 
        return 0

    visited.append((r, c))


def solve():

    visited = []
    """
    total_price =0

    for (i,  row) in enumerate(garden):
        for (j, cell)  in enumerate(row):
            if (i, j) not in visited:
                area, perimeter = find_perimeter_and_area(garden, cell, i, j, visited)
                #print(f"AREA: {area} perimeter: {perimeter}")
                total_price += area * perimeter

    print("PART 1", total_price)

    for (i,  row) in enumerate(garden):
        for (j, cell)  in enumerate(row):
            if (i, j) not in visited:
                find_num_sides(cell, i, j, 0)
    """
    i = 0 
    j = 0
    print(find_num_sides(map, map[i][j], i, j, visited))





solve()




