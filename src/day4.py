from helper import read_file_to_list

board = read_file_to_list("../inputs/day4.txt")

words = ["XMAS", "SAMX"]
WORD_SIZE = len(words[0])
BOARD_SIZE = len(board)
visited = []

def check_rows(board, idx):
    count = 0

    for j in range(len(board)):
        for k in range(j, j+5):
            if (board[idx][j:k]) == words[0] or board[idx][j:k] == words[1]:
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
            if s == words[0] or s == words[1]:
                count += 1
    return count


def check_lower_left(board, r, c):
    s = ""
    count = 0

    # Go along diagonal
    while r <= BOARD_SIZE - 1 and c >= 0:
        s += board[r][c]

        if s == words[0] or s == words[1]:
            origin_r = r - 3
            origin_c = c + 3
            coord_data = (origin_r, origin_c, "LL")

            # Avoid duplicates
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

    # Go along diagonal
    while r <= BOARD_SIZE - 1 and c <= BOARD_SIZE - 1:
        s += board[r][c]

        if s == words[0] or s == words[1]:
            origin_r = r - 3
            origin_c = c - 3
            coord_data = (origin_r, origin_c, "LR")

            # Avoid duplicates
            if coord_data not in visited:
                count += 1
                visited.append(coord_data)

            s = ""

        r += 1
        c += 1
    return count

def check_diagonals(board):
    count = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
                count += check_lower_left(board, row, col)
                count += check_lower_right(board, row, col)

    return count

def check_x(board):
    count = 0
    x1 = ""
    x2 = ""
    
    # Iterate over board
    for row in range(len(board)):
        for col in range(len(board[row])):
            cell = board[row][col]

            # Middle of X pattern
            if (cell == 'A'):
                r = row
                c = col
                up_left = (r - 1 >= 0 and c - 1 >= 0)
                up_right = (r - 1 >= 0 and c + 1 <= BOARD_SIZE - 1)
                down_left = (r + 1 <= BOARD_SIZE - 1 and c - 1 >= 0)
                down_right = (r + 1 <= BOARD_SIZE - 1 and c + 1 <= BOARD_SIZE - 1)

                # Check for X pattern
                if up_left and up_right and down_left and down_right:
                    x1 = board[r-1][c+1] + cell + board[r+1][c-1]
                    x2 = board[r-1][c-1] +  cell + board[r+1][c+1]

                    if (x1 == "MAS" or x1 == "SAM") and (x2 == "MAS" or x2 == "SAM"):
                        count += 1

                    x1 = "" 
                    x2 = ""
    return count



def day1():
    total = 0

    for idx in range(len(board)):
        total += check_rows(board, idx)
        total +=  check_cols(board, idx)
        
    total += check_diagonals(board)

    print("DAY 1: ", total)

def day2():
    total = check_x(board)
    print("DAY 2: ", total)


day1()
day2()
