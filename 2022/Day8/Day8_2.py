try:
    import logging
    import os
    import numpy as np

except:
    print("Imports failed")

TEST = not True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"


def check_row(row, height, pos):
    to_left = row[0:pos]
    to_right = row[pos+1:]

    tree_count_left = view_count(to_left, height, True)
    tree_count_right = view_count(to_right, height, False)

    return tree_count_left, tree_count_right


def check_column(col, height, pos):
    above = col[0:pos]
    below = col[pos+1:]

    tree_count_up = view_count(above, height, True)
    tree_count_below = view_count(below, height, False)

    return tree_count_up, tree_count_below


def view_count(strip, height, left_up):
    tmp = strip.copy().tolist()
    if left_up:
        tmp.reverse()
    count = 0

    for i, value in enumerate(tmp):
        if height >= value:
            count += 1
            if height == value:
                return count
        else:
            count += 1
            return count

    return count
    

def can_be_seen(input):
    
    row = input.shape[0]
    col = input.shape[1]

    sum = np.zeros((row,col), dtype=int)

    for r in range(1,row-1):
        for c in range(1, col-1):
            up, down = check_column(input[:, c], input[r][c], r)
            left,right = check_row(input[r, :], input[r][c], c)
            sum[r][c] = up * down * left * right

    return sum

def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    input = [[int(i) for i in list(x.strip())] for x in input]

    return np.array(input)

def main():
    input = get_input()
    #print(input[1][:])


    r = input.shape[0]
    c = input.shape[1]

    view_score = can_be_seen(input) # find all the inner ones that can be seen

    max = 0
    r_index = 0
    c_index = 0
    prev = 0

    for i in range(r):
        for j in range(c):

            if view_score[i][j] > max:
                max = view_score[i][j]
                r_index = i
                c_index = j

            else:
                continue

    print(max)
    print(str(r_index) + " " + str(c_index))
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")