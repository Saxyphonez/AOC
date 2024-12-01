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


    pattern = re.compile(r"do[(][)]|don't[(][)]|mul[(][0-9]+[,][0-9]+[)]")
    instructions = []
    for line in input:
        print(line)
        instructions.extend(re.findall(pattern, line))

    print(len(instructions))

    pause = False

    mul_pattern = re.compile(r"[0-9]{1,3}")
    sum = 0

    for inst in instructions:
        #print("inst = {}".format(inst))

        capt = re.findall(mul_pattern, inst)
        #print("capt = {}".format(capt))

        if not capt:
            if inst == "don't()":
                #print("pausing")
                pause = True
                continue
            elif inst == "do()":
                #print("unpausing")
                pause = False
                continue
            else:
                print("Error, shouldnt get here!")
            
        else:
            if not pause:
                #print("Adding")
                sum += int(capt[0]) * int(capt[1])
            else:
                #print("skipped")
                pass

    print("Sum = {}".format(sum))
    print("Done!")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
