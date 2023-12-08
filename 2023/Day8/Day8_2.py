try:
    import logging
    import os
    import timeit
    import re
    import numpy as np

except:
    print("Imports failed")

TEST = not True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

START = "A"
END = "Z"
L = 0
R = 1

class Node:
    def __init__(self, name, left, right, is_start = False, is_end = False):
        self.name = name
        self.connections = [left, right]
        self.is_start = is_start
        self.is_end = is_end

    def __repr__(self):
        str = "Node {}: = ({}, {}). Start:{} End:{}".format(self.name, 
                                                           self.connections[L], 
                                                           self.connections[R],
                                                           self.is_start,
                                                           self.is_end)
        return(str)
    
    def __str__(self):
        return(self.__repr__())


def parse_into_dict(nodes_list):
    buf_dict = {}
    start_nodes = []
    end_nodes = []

    for node in nodes_list:
        start = False
        end = False

        pattern = r"([A-Z0-9]{3})"
        node_data = re.findall(pattern, node)

        name = node_data[0]
        left = node_data[1]
        right = node_data[2]

        if re.search(r"(\w{2}[A])", name):
            start = True
        
        if re.search(r"(\w{2}[Z])", name):
            end = True

        node = Node(name, left, right, start, end)
        buf_dict[name] = node

        if start:
            start_nodes.append(name)

        if end:
            end_nodes.append(name)


    return buf_dict, start_nodes, end_nodes

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
    nodes = raw_input[2:]

    #generate a map
    start_nodes = []
    point_map, start_nodes, end_nodes  = parse_into_dict(nodes)

    print("Start nodes = {}".format(start_nodes))
    print("End nodes = {}".format(end_nodes))

    #traverse map
    reached = False

    step_count = 0
    step_counts = []

    for starting in start_nodes:
        reached = False
        step_count = 0
        current_point = point_map[starting]

        while not reached:
            for i, current_dirn in enumerate(dirn):
                #print(current_point)
                step_count+=1
                            
                if current_point.is_end:
                    reached = True
                    break

                if current_dirn == "L":
                    next_point = current_point.connections[L]

                elif current_dirn == "R":
                    next_point = current_point.connections[R]

                
                current_point = point_map[next_point]
                

        #print("{} steps taken".format(step_count-1))
        step_counts.append(step_count-1)

    #find LCM:
    lcm = np.lcm.reduce(np.array(step_counts), dtype=object) #dtype object needed as number was negative otherwise

    print("LCM of {} = {}".format(step_counts, lcm))

    print("done")


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))