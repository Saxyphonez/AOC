try:
    import logging
    import os
    import sys

    # import re
    from board import *

except ModuleNotFoundError or ImportError as e:
    print("Imports failed")
    print(e)

TEST = not True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    input = [list(line.strip()) for line in input]
    return input

def main():

    print("Test is {}".format(TEST))
    input = get_input()
    num_rows = len(input)
    num_cols = len(input[0])


    map = Board(rows = num_rows, cols = num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            map.cells[r][c] = 1 if input[r][c] == "@" else 0


    map.render()

    #print(map.get_neighbours(0,2))
    # 0 is space
    # 1 is roll
    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if map.cells[r][c] == 0:
                continue

            neighbours = map.get_neighbours(r,c)

            if neighbours.count(1) < 4:
                count += 1
            else:
                continue
    
    print("Count = {}".format(count))

    print("Done!")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
