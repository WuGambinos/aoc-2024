from helper import read_file_to_list

board = read_file_to_list("../inputs/day4.txt")

words = ["XMAS", "SAMX"]
WORD_SIZE = 4
BOARD_SIZE = len(board)
visited = []




def check_rows(board, idx):
    count = 0

    for j in range(len(board)):
        for k in range(j, j+5):
            if (board[idx][j:k]) in words:
                count += 1

    return count

def check_cols(board, idx):
    count = 0
    s = ""
    for j in range(len(board)):
        for k in range(j, j+5):
            s = ""
            for l in range(j, k):
                if k > len(board):
                    break
                s += board[l][idx]
            if s in words:
                count += 1
    return count

def check_upper_left(board, r, c):
    s = ""
    count = 0
    curr_visit = []
    while r >= 0 and c >= 0:
        s += board[r][c]
        curr_visit.insert(0, (r, c))

        if s in  words and curr_visit not in visited:
            visited.append(curr_visit)
            print(f"UPPER LEFT({r} {c}): {s}")
            print(f"UPPER LEFT: VISITED: {curr_visit}")
            print()
            count += 1
            s = ""
        elif len(s) == 4:
            curr_visit = []

        r -= 1
        c -= 1
    return count

def check_upper_right(board, r, c):
    s = ""
    count = 0
    curr_visit = []
    while r >= 0 and c <= BOARD_SIZE - 1:
        s += board[r][c]
        curr_visit.insert(0, (r, c))
        if s in  words and curr_visit not in visited:
            visited.append(curr_visit)
            print(f"UPPER RIGHT({r} {c}): {s}")
            print(f"UPPER RIGHT: VISITED: {curr_visit}")
            print()
            count += 1
            s = ""
        elif len(s) == 4:
            curr_visit = []

        r -= 1
        c += 1
    return count

def check_lower_left(board, r, c):
    s = ""
    count = 0
    curr_visit = []
    while r <= BOARD_SIZE - 1 and c >= 0:
        s += board[r][c]
        curr_visit.append((r, c))
        if s in  words and curr_visit not in visited:
            visited.append(curr_visit)
            print(f"LOWER LEFT: ({r} {c}): {s}")
            print(f"LOWER LEFT: VISITED: {curr_visit}")
            print()
            count += 1
            s = ""
        elif len(s) == 4:
            curr_visit = []

        r += 1
        c -= 1
    return count

def check_lower_right(board, r, c):
    s = ""
    count = 0
    curr_visit = []
    while r <= BOARD_SIZE - 1 and c <= BOARD_SIZE - 1:
        s += board[r][c]
        curr_visit.append((r, c))

        if s in  words and curr_visit not in visited:
            visited.append(curr_visit)
            print(f"LOWER RIGHT: ({r} {c}): {s}")
            print(f"LOWER RIGHT: VISITED: {curr_visit}")
            print()
            count += 1
            s = ""
        elif len(s) == 4:
            curr_visit = []

        r += 1
        c += 1
    return count




def check_diagonals(board):
    count = 0
    upper_left_total = 0
    upper_right_total = 0

    lower_left_total = 0
    lower_right_total = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if row >= WORD_SIZE - 1 and col >= WORD_SIZE - 1:
                upper_left_total += check_upper_left(board, row, col)
                upper_right_total += check_upper_right(board, row, col)
                lower_left_total += check_lower_left(board, row, col)
                lower_right_total += check_lower_right(board, row, col)

    count += upper_left_total + upper_right_total + lower_left_total + lower_right_total
    print(f"UPPER LEFT: {upper_left_total} UPPER_RIGHT: {upper_right_total}")
    print(f"LOWER LEFT: {upper_left_total} LOWER_RIGHT: {upper_right_total}")

    return count



def day1():
    total = 0
    horiz_total = 0
    vert_total = 0

    for idx in range(len(board)):
        horizontal = check_rows(board, idx)
        vertical  = check_cols(board, idx)
        total += vertical + horizontal
        horiz_total += horizontal 
        vert_total += vertical
        
    #check_diagonals(board)
    total += check_diagonals(board)


    print("HORIZONTAL: ", horiz_total, "VERTICAL", vert_total)
    print("DAY 1: ", total)


day1()
    


