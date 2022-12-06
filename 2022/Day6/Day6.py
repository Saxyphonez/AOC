try:
    import logging
    import os

except:
    print("Imports failed")

TEST = not True
MARKER_LENGTH = 4

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

    input = [list(x.strip()) for x in input]
    return input

def find_marker(input):
    input_len = len(input)
    four_char_buf = []

    for i in range(input_len):
        four_char = input[i:i+MARKER_LENGTH]

        if len(set(four_char)) == MARKER_LENGTH:
            return i+MARKER_LENGTH
        else:
            continue


def main():

    input =  get_input()
    #print(input)
    for i, val in enumerate(input):
        loc = find_marker(val)
        print(loc)
    #answers for test:
    #5,6,10,11
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")