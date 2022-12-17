try:
    import logging
    import os
    import re

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

    input = [x.strip() for x in input]

    return input


def check_cycle_count(clk_cnt, reg_X):

    if clk_cnt == 20 or (clk_cnt-20)%40 == 0:
        #print("Clk count = " + str(clk_cnt) + ", X = " + str(reg_X))
        return clk_cnt*reg_X

    else:
        return 0

    

def main():
    instructions = get_input()
    reg_X = 1
    clk = 0
    sum = 0
    crt = []

    for i, op in enumerate(instructions):

        if op == 'noop':
            if clk%40 == reg_X - 1 or clk%40 == reg_X or clk%40 == reg_X +1:
                crt.append("#")
            else:
                crt.append(".")
            clk += 1
            sum += check_cycle_count(clk, reg_X)
            continue

        else:
            op_split = op.split(" ")
            
            if clk%40 == reg_X - 1 or clk%40 == reg_X or clk%40 == reg_X +1:
                crt.append("#")
            else:
                crt.append(".")
            clk += 1
            sum +=check_cycle_count(clk, reg_X)   
            
            if clk%40 == reg_X - 1 or clk%40 == reg_X or clk%40 == reg_X +1:
                crt.append("#")
            else:
                crt.append(".")
            clk += 1
            sum +=check_cycle_count(clk, reg_X)
            reg_X += int(op_split[1])


    for i, px in enumerate(crt):
        if i%40 == 0:
            print(" ")

        print(px, end="")
    

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")