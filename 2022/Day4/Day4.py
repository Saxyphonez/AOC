try:
    import logging
    import os

except:
    print("Imports failed")

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

    output = []
    for i, values in enumerate(input):
        buffer = values.strip().split(",")

        for j, nums in enumerate(buffer):
            tmp = nums.split("-")
            
            output.append([int(x) for x in tmp])

    
    return output

def find_overlap(range_first, range_second):
    if len(range_first) == 1:
        first_num = set(range_first[0])
        second_num = set(range(range_second[0], range_second[1]+1))

    elif len(range_second) ==1:
        second_num = set(range_second[0])
        first_num = set(range(range_first[0], range_first[1]+1))

    else:
        first_num = list(range(range_first[0], range_first[1]+1))
        second_num = list(range(range_second[0], range_second[1]+1))

    overlaps = list(set(first_num).intersection(second_num))
    if len(overlaps) == len(first_num) or len(overlaps) == len (second_num):
        return 1
    else:
        return 0

def main():

    input = get_input()
    #print(input)
    iterations_needed = int(len(input)/2)

    overlaps = 0
    for i in range(iterations_needed):
        overlaps += find_overlap(input[2*i], input[(2*i)+1])

    print(overlaps)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")