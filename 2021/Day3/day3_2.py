try:
    import logging
    import os
    import numpy as np

except:
    print("Imports failed")

TEST = True

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

    for i,value in enumerate(input):
        input[i] = value.strip()
    
    bianry_arr = split_binary(input)
    return bianry_arr

def split_binary(binary_nums):
    length = len(binary_nums[0])
    arr = []

    for i,value in enumerate(binary_nums):
        arr.insert(i, list(value))
    
    #print(arr)
    
    return np.array(arr)

def find_occurence(binary_arr, oxy, carbo):
    zero_occur = 0
    one_occur = 0
    rows, columns = binary_arr.shape
    #row = shape(1)
    #columns = shape(2)
    gamma = np.empty(columns)
    epsilon = np.empty(columns)

    for c in range(columns):
        for r in range(rows):
            value = int(binary_arr[r][c])
            if value == 0:
                zero_occur += 1

            elif value == 1:
                one_occur += 1

            else:
                logging.error("Issue determinig 1 or 0")

        if zero_occur > one_occur:
            gamma[c] = 0
            epsilon[c] = 1

        elif one_occur > zero_occur:
            gamma[c] = 1
            epsilon[c] = 0

        elif one_occur == zero_occur:
            if oxy:
                gamma[c] = 1 #keep values with a 1
            else:
                epsilon[c]=0 #keep values with a 0
        else:
            logging.error("Cannot compare occurences")

        zero_occur = 0
        one_occur = 0

    return gamma, epsilon

def BtD(binary_arr):
    dec = 0

    for i, value in enumerate(binary_arr):
        dec = int(value) << len(binary_arr) - i-1 | dec

    return dec

def find_rating(binary_array, oxy, carbo):
    buffer = binary_array
    #rating = []
    posn = 0

    while len(buffer) > 1:
        rows, columns = buffer.shape
        #if oxy:
        #gamma oxy, epsilon carbo
        gamma, epsilon = find_occurence(buffer, True, False) #(buf, oxy, carbo)
        buffer = matching_values(buffer, posn, gamma[posn])
        

    return buffer

def matching_values(arr, pos, match_val):
    #buffer = np.empty((1,arr.shape[1]))

    for i in range(len(arr)):
        value_int = int(arr[i][pos])

        if value_int == match_val:
            buffer = np.concatenate(buffer,arr[i])
    
    return buffer


def main():

    binary_array = get_input()
    #gamma, epsilon = find_occurence(binary_array)
    
    oxy = find_rating(binary_array, True, False)
    #carbo = find_rating(binary_array, False, True)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")