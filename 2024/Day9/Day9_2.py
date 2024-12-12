try:
    import logging
    import os
    import sys

    # import re
    from customTypes import *

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
    

    drive = Drive()
    drive_vis = []
    file_id_count = 0

    for i, val in enumerate(input):
        head = len(drive_vis)
        tail = head + val -1

        if (i%2): #if odd
            drive_vis.extend("."*val)

            drive.addFile(File(size = val, head = head, tail = tail))

        else: #if even
            drive_vis.extend([file_id_count]*val)
            drive.addFile(File(id=file_id_count, size = val, type = FileType.REALFILE,
                              head = head, tail = tail))
            
            file_id_count +=1


    #pretty_print(drive.files[-1])
    print(drive.files[-1])
    #pretty_print(drive_vis)
    # pretty_print(defragged)

    operation(drive=drive)

    # print(checksum(defragged))

    print("Done!")


def checksum(defrag):
    checksum = 0

    for i,val in enumerate(defrag):
        if val == ".":
            continue
        else:
            checksum += i*int(val)


    return checksum


def operation(drive):

    memoryMap = drive.addressTable.copy()

    #iterate over the memory


    pass


def pretty_print(lis):

    for val in lis:
        print(val, end="")
    print("")

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
