try:
    import logging
    import os
    import sys

    # import re

except ModuleNotFoundError or ImportError as e:
    print("Imports failed")
    print(e)

TEST = not True

CELL_COUNT_MAX = 12

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



def generate_banks(input):

    split = [list(line) for line in input]
    banks = []

    for item in split:
        bank = [int(x) for x in item]
        banks.append(bank)

    return banks


def find_largest_joltage(bank):
    big_jolt = 0

    contending_jolts = []

    # given a list, I want to find
    # the largest value and it's position

    # special cases:
    # if the first go, then we can't be in last position
        # if cell_count == 0: continue

    # if we are on the last cell (cell 12), we can allow that
        # if cell_count ==  12: 

    total_len = len(bank)

    subset = bank # This decreases with every cell count
    subset_index = 0
    subset_len = len(subset)

    for cell_count in range (1, CELL_COUNT_MAX+1):
        
        subset_len = len(subset)

        for j in range (9, 0, -1):
            try:
                tmp_pos = subset.index(j)
            except ValueError:
                continue
            
            if cell_count == 1:
                if tmp_pos == (subset_len-1):
                    continue
                else:
                    if len(subset[tmp_pos+1:]) < CELL_COUNT_MAX-cell_count:
                        continue
                    else:        
                        contending_jolts.append(j)
                        subset_index = tmp_pos
                        break

            elif cell_count == CELL_COUNT_MAX:
                contending_jolts.append(j)
                break

            else:
                if len(subset[tmp_pos+1:]) < CELL_COUNT_MAX-cell_count:
                    continue
                else:        
                    contending_jolts.append(j)
                    subset_index = tmp_pos
                    break
        
        # shrink the bank
        subset = subset[subset_index+1:]


    contending_jolts = [str(x) for x in contending_jolts]
    big_jolt = int(''.join(contending_jolts))
    
    return big_jolt



def main():

    print("Test is {}".format(TEST))
    input = get_input()

    banks = generate_banks(input)

    joltages = []

    for i, bank in enumerate(banks):
        joltages.append(find_largest_joltage(bank))

    if TEST:
        print(joltages)

    sum = 0
    for joltage in joltages:
        sum += joltage

    print("Sum = {}".format(sum))

    if TEST:
        if sum != 3121910778619:
            print("BAD CODE")
    else:
        print("Done!")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
