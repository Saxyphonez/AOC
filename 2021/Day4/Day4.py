try:
    import logging
    import os
    import pandas as pd

except:
    print("Imports failed")

TEST = True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

def get_input():
    #boards = pd.DataFrame()

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()


    numbers_called = input[0].strip().split(",")
    input.pop(0)

    buffer = []
    buffer_board_status = []

    for i, value in enumerate(input):
        if value == '\n':
            #input.pop(i)
            continue
        else:
            val = value.strip().split(" ")
            val = [i for i in val if i]
            buffer.append(val)
            buffer_board_status.append([0]*len(val))


    return numbers_called, buffer, buffer_board_status


def call_number(number, boards, boards_status):

    for i, val in enumerate(boards):
        for j, value in enumerate(val):

            if value == number:
                boards_status[i][j] = 1
                win = check_for_done(boards_status)

                if win:
                    return number, boards, boards_status, win

    return number, boards, boards_status, win

def check_for_done(boards):
    row_sums=[]
    col_sums=[]
    iter_needed = int((len(boards)+1)/5)

    for iteration in range(iter_needed):
        current_board = boards[iteration*5:(iteration*5)+5]
        r_sum = [sum(i) for i in current_board]
        c_sum = [sum(x) for x in zip(*current_board)]
        row_sums.append(r_sum)
        col_sums.append(c_sum)

    if any(5 in nested for nested in row_sums) or any(5 in nested for nested in  col_sums):
        return True
    else:
        return False


def main():
    numbers_called, boards, boards_status = get_input()
    win = False
    for number in numbers_called:
        if not win:
            number, boards, boards_status, win = call_number(number, boards, boards_status)
        else:
            break

    print(number)
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")