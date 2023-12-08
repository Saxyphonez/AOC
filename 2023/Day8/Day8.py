try:
    import logging
    import os
    import timeit
    import re

except:
    print("Imports failed")

TEST = not True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

START = "AAA"
END = "ZZZ"
L = 0
R = 1


def parse_into_dict(nodes_list):
    buf_dict = {}
    for node in nodes_list:
        pattern = r"([A-Z]{3})"
        node_data = re.findall(pattern, node)

        name = node_data[0]
        left = node_data[1]
        right = node_data[2]

        buf_dict[name] = [left, right]

    return buf_dict

def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    input = [line.strip() for line in input]
    return input

def main():
    raw_input = get_input()

    dirn = list(raw_input[0])
    nodes = raw_input[2:-1]

    #generate a map
    map = parse_into_dict(nodes)


    #traverse map
    reached = False
    current_point = START
    last_pass_end_point = START

    step_count = 0

    while not reached:
        for i, current_dirn in enumerate(dirn):
            print(current_point)
            step_count+=1

            if current_point == END:
                reached = True
                break

            if current_dirn == "L":
                next_point = map.get(current_point)[L]

            elif current_dirn == "R":
                next_point = map.get(current_point)[R]

            
            current_point = next_point

    print("{} steps taken".format(step_count-1))
    print("done")


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))