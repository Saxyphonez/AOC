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

    break_loc = input.index("")

    orders = input[:break_loc]
    updates = input[break_loc+1:]

    correct = [False]*len(updates)

    orders = parse_orders(orders)
    updates = parse_updates(updates)

    # print(orders)
    # print(updates)
    total = 0
    for i, line in enumerate(updates):
        if(check(line, orders)):
            correct[i] = True
            total+=1
        else:
            continue

    tmp = []
    sum = 0
    for i, status in enumerate(correct):
        if(status):
            tmp = updates[i]
            sum += tmp[int((len(tmp)-1)/2)]

        else:
            continue

    print(sum)
    print("Done!")

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
