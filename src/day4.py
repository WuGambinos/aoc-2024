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


def check_lower_left(board, r, c):
    s = ""
    count = 0
    while r <= BOARD_SIZE - 1 and c >= 0:
        s += board[r][c]
        if s in  words:
            coord_data = (r-3, c+3, "LL")
            if coord_data not in visited:
                count += 1

            visited.append(coord_data)
            s = ""

        r += 1
        c -= 1
    return count

def check_lower_right(board, r, c):
    s = ""
    count = 0
    while r <= BOARD_SIZE - 1 and c <= BOARD_SIZE - 1:
        s += board[r][c]

        if s in  words:
            coord_data = (r-3, c-3, "LR")
            if coord_data not in visited:
                count += 1

            visited.append(coord_data)
            s = ""

        r += 1
        c += 1
    return count

def check_diagonals(board):
    count = 0

    lower_left_total = 0
    lower_right_total = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
                lower_left_total += check_lower_left(board, row, col)
                lower_right_total += check_lower_right(board, row, col)


    count +=  lower_left_total + lower_right_total
    return count



def day1():
    total = 0

    for idx in range(len(board)):
        total += check_rows(board, idx)
        total +=  check_cols(board, idx)
        
    total += check_diagonals(board)

    print("DAY 1: ", total)

def day2():
    total = 0
    print("DAY 2: ", total)


day1()
day2()
    


