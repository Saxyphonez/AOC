try:
    import logging
    import os
    import sys
    import math

    import re

except ModuleNotFoundError or ImportError as e:
    print("Imports failed")
    print(e)

TEST = not True


MIN_DIAL_VAL = 0
MAX_DIAL_VAL = 99
DIAL_START = 50

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

    input = [line.strip() for line in input]
    return input

def main():

    print("Test is {}".format(TEST))
    input = get_input()


    dial_position = DIAL_START
    prev_dial_position = dial_position
    count = 0


    dir_pattern = re.compile(r"[lrLR]")
    amount_pattern = re.compile(r"[0-9]+")

    for idx, inst in enumerate(input):
        prev_dial_position = dial_position
       

        # Extract direction and number of clicks
        dir = re.search(dir_pattern,inst).group()
        amount =int(re.search(amount_pattern,inst).group())

        if dir == "L":
            for i in range (0,amount):
                dial_position -= 1
                dial_position = dial_position % (MAX_DIAL_VAL+1)

                if 0 == dial_position:
                    count += 1
        else:
            # dial_position += amount
            for i in range (0,amount):
                dial_position += 1
                dial_position = dial_position % (MAX_DIAL_VAL+1)

                if 0 == dial_position:
                    count += 1
        
        print("[{}]\t{} -> {} ({}). Zero count: {}".format(idx, prev_dial_position, dial_position, inst, count))


        
    print("Count of zeros {}".format(count))


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
