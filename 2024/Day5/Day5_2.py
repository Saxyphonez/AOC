try:
    import logging
    import os
    import sys

    #import re

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

    break_loc = input.index("")

    orders = input[:break_loc]
    updates = input[break_loc+1:]

    correct = [False]*len(updates)

    orders = parse_orders(orders)
    updates = parse_updates(updates)

    #order_comes_after, order_comes_before = graph_orders(orders)
   
    #find maximum number of pages in a line
    # max = 0
    # for i, line in enumerate(updates):
    #     if(len(line) > max):
    #         max = len(line)

    #Find out which update lines match the rules
    for i, line in enumerate(updates):
        if(check(line, orders)):
            correct[i] = True
            #total+=1
        else:
            continue

        



        
    #perform operations on ones that do not match the rules
    corrected = []
    for i, status in enumerate(correct):
        if status:
            continue
        
        #miracle here
        corrected.append(fix(updates[i], orders))

    print(corrected)



    # do  the addition of middle numbers
    sum = 0
    for i, line in enumerate(corrected):
        sum += line[int((len(line)-1)/2)]


    print(sum)
    print("Done!")


def graph_orders(orders):
    #turn orders into a graph
    graph_after = {} # what has to be after a number
    graph_before = {} # what has to be before a number

    
    for i, order in enumerate(orders):
        node = order[0]
        neighbour = order[1]
        if node in graph_after:
            graph_after[node].add(neighbour)
            
        else:
            graph_after[node] = set()
            graph_after[node].add(neighbour)


        if neighbour in graph_before:
            graph_before[neighbour].add(node)
        else:
            graph_before[neighbour] = set()
            graph_before[neighbour].add(node)

    return graph_after, graph_before

def fix(line, orders):
    line_local = line.copy()

    applicable_orders = []
    for page in line_local:
        for order in orders:
            if (page in order) and (order not in applicable_orders):
                applicable_orders.append(order)
            else:
                continue
    
    order_comes_after, order_comes_before = graph_orders(applicable_orders)

    changes_made = True
    while (changes_made):
        changes_made = False

        for order in applicable_orders:
            status, first_loc, second_loc = check_against_rule(line_local, order)
            if(status == 1):
                continue
            elif(status == 0):
                #perform a swap
                line_local[first_loc] = order[1]
                line_local[second_loc] = order[0]
                changes_made = True
            else:
                #print("ValueErr so skipping")
                continue

    #print(line_local)
    if TEST:
        print("{} -(fix)-> {}".format(line, line_local))

    return(line_local)


def check_against_rule(line, order):
    #checks a single line against a single rule
    before = order[0]
    after = order[1]

    try:
        loc_before = line.index(before)
        loc_after = line.index(after)

        if loc_before < loc_after:
            return 1, loc_before, loc_after
        else:
            return 0, loc_before, loc_after
        
    except ValueError:
        #print("ValueError!")
        return -1, None, None


def check(line, orders):

    for i, order in enumerate(orders):
        before = order[0]
        after = order[1]

        try:
            loc_before = line.index(before)
            loc_after = line.index(after)

            if loc_before < loc_after:
                continue
            else:
                return False
            
        except ValueError:
            continue

    return True
    
def parse_orders(orders):
    buf = orders.copy()

    buf = [x.split("|") for x in buf]
    for i, pair in enumerate(buf):
        tmp = [int(x) for x in pair]
        buf[i] = tmp

    return buf

def parse_updates(updates):
    buf = updates.copy()
    buf = [x.split(",") for x in buf]

    for i, line in enumerate(buf):
        tmp = [int(x) for x in line]
        buf[i] = tmp

    return buf

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
