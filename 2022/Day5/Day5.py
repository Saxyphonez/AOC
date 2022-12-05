try:
    import logging
    import os
    import pandas as pd
    import re
    import numpy as np

except:
    print("Imports failed")

TEST = True


if TEST:
    input_filename = "test_input.txt"
    NUM_OF_STACK = 3
else:
    input_filename = "input.txt"
    NUM_OF_STACK = 9

def get_input():
    input = []
    buffer = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    break_index = input.index("\n")

    stacks_raw = input[0:break_index-1]
    moves_raw = input[break_index+1:]

    moves = []
    for i, value in enumerate(moves_raw):
        tmp = re.findall(r'\b\d+\b', value)
        tmp2 = [int(x) for x in tmp]
        moves.append(tmp2.copy())
        tmp2.clear()


    return stacks_raw, moves


def make_stacks(raw_input):
    stack = []

    for i, value in enumerate(raw_input):
        raw_input[i] = value.replace("\n", " ")

    clean_stack = clean_stack_items(raw_input)
    iterations_needed = int(clean_stack.shape[0])

    #take clean_stack and split into separate columns
    for i in range(iterations_needed):
        stack.append(clean_stack[:,i])

    return stack

def clean_stack_items(dirty):
    clean_buf = []
    length = int(len(dirty[0])/4)

    for i, value in enumerate(dirty):
        for j in range(length):
            tmp = value[4*j:(4*j)+4]

            if re.match(r"\s{4}",tmp):
                clean_buf.append(" ")

            elif re.match(r"\[(.*?)\]",tmp):
                letter = re.match(r"\[(.*?)\]",tmp).string
                clean_buf.append(letter.strip())

    clean = np.reshape(clean_buf, (NUM_OF_STACK, -1))
    return clean

def main():

    stacks_raw, moves = get_input() 
    stack = make_stacks(stacks_raw)
    #moves = [from stack num, amount, to stack num]
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")