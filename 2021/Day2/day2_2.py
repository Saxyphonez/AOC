try:
    import logging
    import os
    from array import *
except:
    print("Imports failed")


def get_input():
    directions_split = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    #f.close()

    for i,value in enumerate(input):
        instructions = value.split(" ")
        instructions[1] = int(instructions[1].strip())
        directions_split.insert(i,instructions)

    return directions_split

def print_array(arr):
    for m in arr:
        for n in m:
            print(n,end = " ")
        print()

def main():
    directions = get_input()
    depth = 0
    horiz = 0
    aim = 0

    for index, value in enumerate(directions):
        instruction = value[0]
        num = value[1]

        if instruction == 'forward':
            horiz += num
            depth += aim*num

        elif instruction == 'down':

            aim += num
            
        elif instruction == 'up':
            aim -= num

        else:
            logging.error("Instruction not understood")
    
    mult = depth * horiz
    print(mult)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")