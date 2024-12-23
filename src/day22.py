f = open('../inputs/day22_part2test.txt')

secret_numbers = []

for line in f:
    #print(line.strip())
    secret_numbers.append(int(line.strip()))

def gen_secret_num(secret_num):
    n1 = secret_num * 64 
    secret_num = n1 ^ secret_num
    secret_num = secret_num % 16777216

    n2 = secret_num // 32
    secret_num = n2 ^ secret_num
    secret_num = secret_num % 16777216

    res = secret_num * 2048
    secret_num ^= res
    secret_num = secret_num % 16777216

    return secret_num

"""
def find_unqiue_sequences(n):

    prices = []
    ITERATIONS = 2000
    prev_digit = n % 10
    prices.append(prev_digit)

    changes = 0 
    prev_diff = None

    unqiue_sequences = []
    seq = []
    for _ in range(0, ITERATIONS - 1):
        n = gen_secret_num(n)
        digit = n % 10
        prices.append(digit)

        diff = digit - prev_digit
        print("DIGIT: ", digit, "DIFF: ", diff, "CONSEC CHANGES", changes)
    
        # Hiding spot found, move onto next buyer
        if changes == 4:
            changes = 0
            seq.append(diff)
            unqiue_sequences.append((digit, seq))
            seq = []
        
        # Track Previous Difference
        if prev_diff != None:
            if diff != prev_diff:
                if changes == 4:
                    changes = 0
                    seq.append(diff)
                    unqiue_sequences.append((digit, seq))
                    seq = []

                if changes != 0:
                    seq.append(diff)
                changes += 1
            else:
                changes = 0
                seq = []
        else:
            prev_diff = diff

        prev_digit = digit

    return unqiue_sequences
"""

def find_unqiue_sequences(n):

    ITERATIONS = 2000
    prev_digit = n % 10

    changes = 0 
    prev_diff = None

    unqiue_sequences = []
    seq = []
    for _ in range(0, ITERATIONS - 1):
        n = gen_secret_num(n)
        digit = n % 10

        diff = digit - prev_digit
        #print("DIGIT: ", digit, "DIFF: ", diff, "CONSEC CHANGES", changes)
    
        """
        # Hiding spot found, move onto next buyer
        if changes == 4:
            changes = 0
            seq.append(diff)
            unqiue_sequences.append((digit, seq))
            seq = []
        """
        
        # Track Previous Difference
        if prev_diff != None:
            print("PREV_DIGIT: ", prev_digit, "DIGIT: ", digit, "PREV_DIFF" , prev_diff, "DIFF: ", diff, "CONSEC CHANGES", changes)
            if diff != prev_diff:
                if changes == 4:
                    changes = 0
                    seq.append(diff)
                    unqiue_sequences.append((digit, seq))
                    seq = []

                if changes != 0:
                    seq.append(diff)

                changes += 1
            else:
                changes = 0
                seq = []
            prev_diff = diff
        else:
            print("PREV_DIGIT: ", prev_digit, "DIGIT: ", digit, "PREV_DIFF" , prev_diff, "DIFF: ", diff, "CONSEC CHANGES", changes)
            if digit != prev_digit:
                changes += 1

            prev_diff = diff

        prev_digit = digit

    return unqiue_sequences

def solve(part1):


    if part1:
        result = []
        ITERATIONS = 2000
        for i in range(len(secret_numbers)):
            n = secret_numbers[i]
            for _ in range(0, ITERATIONS):
                n = gen_secret_num(n)
            result.append(n)
        print("PART 1", sum(result))
    else:
        """
        for i in range(len(secret_numbers)):
            n = secret_numbers[i]
            for _ in range(0, ITERATIONS):
                prices.append(n % 10)
                n = gen_secret_num(n)
                prices.append
            #result.append(n)
        """

        unique = find_unqiue_sequences(1)
        for (price, sequence) in unique:
            if sequence == [-2, 1, -1, 3]:
                print("PRICE: ", price, "SEQ: ", sequence)
        print()


        """
        for num in secret_numbers:
            unique = find_unqiue_sequences(num)
            for (price, sequence) in unique:
                print("PRICE: ", price, "SEQ: ", sequence)
            print()
        """

        """
        (unique, amount) = find_unqiue_sequences(123);
        print("NUMS TO SELL", max(amount))

        for sequence in unique:
            print("SEQ: ", sequence)
        """


        print("PART 2")

#solve(True)
solve(False)
