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

    input = [line.strip() for line in input]
    return input

def main():

    print("Test is {}".format(TEST))
    input = get_input()


    pattern = re.compile(r"mul[(][0-9]+[,][0-9]+[)]")
    collection = []
    for item in input:
        collection.extend(re.findall(pattern, item))

    mul_pattern = r"[0-9]+[,][0-9]+"

    operations = []
    for item in collection:
        opreators = re.findall(mul_pattern, item)
        operations.extend(opreators)

    #print(operations)
    #print(collection)
    sum = 0
    for operation in operations:
        nums = operation.split(",")

        sum += int(nums[0]) * int(nums[1])

    print(sum)
    print("Done!")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
