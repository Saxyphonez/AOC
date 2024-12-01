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

def main():

    print("Test is {}".format(TEST))
    input = get_input()
    list_one = []
    list_two = []

    for item in input:
        ids = item.split(" ")
        list_one.append(int(ids[0]))
        list_two.append(int(ids[3]))
    
    list_one.sort()
    list_two.sort()

    sum=0
    for i, item in enumerate(list_one):
        sum+= abs(item - list_two[i])

    print(sum)
    print("Done!")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
