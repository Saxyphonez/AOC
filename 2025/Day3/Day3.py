try:
    import logging
    import os
    import sys

    # import re

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

    max_pos = 0
    max_val = 0

    next_max_val = 0
    next_max_pos = 0

    total_len = len(bank)

    for i in range (9, 0, -1):
        try:
            tmp_pos = bank.index(i)
        except ValueError:
            continue

        if tmp_pos == (total_len-1):
            continue
        else:
            max_pos = tmp_pos
            max_val = i
            break
    
    #print("Max: {} @ {}".format(max_val, max_pos))

    bank_remaining = bank[max_pos+1:]
    total_len = len(bank_remaining)

    for i in range (9, 0, -1):
        try:
            tmp_pos = bank_remaining.index(i)
        except ValueError:
            continue

        next_max_pos = tmp_pos
        next_max_val = i
        break

    #print("Next: {} @ {}".format(next_max_val, next_max_pos))

    big_jolt = (max_val*10) + next_max_val

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

    print("Done!")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
