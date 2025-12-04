try:
    import logging
    import os
    import sys

    import re

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

    input = [line.strip().split(",") for line in input]
    return input[0]


def get_range(id_range):
    temp = id_range.split("-")

    lower = int(temp[0])
    upper = int(temp[1])

    return (lower, upper)


def find_invalid_ids(id_range:tuple):

    repeating_pattern = re.compile(r"^(.+?)\1+$")

    invalid_ids = []

    for num in range (id_range[0], id_range[1]+1):
        result = re.search(repeating_pattern, str(num))

        if result:
            hit = result.group()

            if num == int(hit):
                invalid_ids.append(int(hit))

    
    return invalid_ids




def main():

    print("Test is {}".format(TEST))
    input = get_input()

    ranges = []
    for i, item in enumerate(input):
        ranges.append(get_range(item))

    #print(ranges)

    invalid_ids = []
    for i, id_range in enumerate(ranges):
        print("Checking range {}".format(id_range))
        invalid_ids.extend(find_invalid_ids(id_range))



    if TEST: 
        print(invalid_ids)

    sum = 0
    for num in invalid_ids:
        sum += num

    print(sum)
    print("Done!")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
