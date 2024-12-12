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
    input = list(input[0])
    input = [int(x) for x in input]
    

    drive = []
    file_id_count = 0

    for i, val in enumerate(input):
        if (i%2): #if odd
            drive.extend("."*val)

        else: #if even
            drive.extend([file_id_count]*val)
            file_id_count +=1


    defragged = defragment(input=input, drive=drive)

    pretty_print(drive)
    pretty_print(defragged)


    print(checksum(defragged))

    print("Done!")


def checksum(defrag):
    checksum = 0

    for i,val in enumerate(defrag):
        if val == ".":
            continue
        else:
            checksum += i*int(val)


    return checksum


def defragment(input, drive):
    drive_local = drive.copy() # 

    total_free_spaces = 0
    for i,val in enumerate(input):
        if (i%2):
            total_free_spaces += val
        else:
            continue

    ptr_next_free_space = input[0] #where is the next place to put a part of a file
    ptr_next_data_to_move = len(drive_local)-1

    end_condition = list("."*total_free_spaces)

    while drive_local[(-1*total_free_spaces):] != end_condition:
        data, space = drive_local[ptr_next_data_to_move], drive_local[ptr_next_free_space]

        drive_local[ptr_next_free_space] = data
        drive_local[ptr_next_data_to_move] = space

        while drive_local[ptr_next_free_space] != ".":
            ptr_next_free_space +=1

        while drive_local[ptr_next_data_to_move] == ".":
            ptr_next_data_to_move -=1



    return drive_local

def pretty_print(lis):

    for val in lis:
        print(val, end="")
    print("")

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
