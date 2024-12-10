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

    input = [x.split(" ") for x in input]

    #remove colon:
    for x in input:
        x[0] = x[0][:-1]

    equations = [[int(y) for y in x] for x in input] # make int

    equation_possible = []
    true_count = 0

    # Does the equation work
    for i,equation in enumerate(equations):
        if is_possible(equation):
            equation_possible.append(True)
            true_count +=1
        else:
            equation_possible.append(False)
            continue

    #do the final summing
    sum = 0
    for i, status in  enumerate(equation_possible):
        if status:
            sum += equations[i][0]
        else:
            #sum += check_concat(equations[i])
            continue
   
    
    print(equation_possible)
    print("num of true: {}".format(true_count))
    print("Sum = {}".format(sum))
    print("Done!")





def is_possible(equation):
    target = equation[0]
    operands = equation[1:]
    total_operands = len(operands)

    count = 0

    layer_vals = []
    big_list = []
    while count < total_operands-1:
        layer_vals_buf = []
        op = operands [count+1]
        
        if count == 0:
            layer_vals_buf.append(operands[count] * op)
            layer_vals_buf.append(operands[count] + op)
            layer_vals_buf.append(int(str(operands[count]) + str(op)))
            layer_vals.append(layer_vals_buf)

        else:
            for val in layer_vals[count-1]:
                layer_vals_buf.append(val * op)
                layer_vals_buf.append(val + op)
                layer_vals_buf.append(int(str(val) + str(op)))

            layer_vals.append(layer_vals_buf)

        count += 1


    big_list.extend(layer_vals_buf)

    if(target in big_list):
        return True
    else: 
        return False



if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
