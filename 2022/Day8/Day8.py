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

    if height > np.amax(to_left) or height > np.amax(to_right):
        return True
    else:
        return False


def check_column(col, height, pos):
    above = col[0:pos]
    below = col[pos+1:]

    if height > np.amax(above) or height > np.amax(below):
        return True
    else:
        return False


def can_be_seen(input):
    sum = 0
    #print(input.shape)
    row = input.shape[0]
    col = input.shape[1]

    for r in range(1,row-1):
        for c in range(1, col-1):
            #print(input[r][c])
            if check_row(input[r, :], input[r][c], c) or check_column(input[:, c], input[r][c], r):
                #print(r, end=" ")
                #print(c, end=" ")
                #print(input[r][c], end=" ")
                #print()
                sum +=1
            else:
                continue
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

    perimeter = ((2*r) + 2*(c-2))
    #print(perimeter)

    how_many = can_be_seen(input) # find all the inner ones that can be seen
    print(how_many+perimeter)

    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")