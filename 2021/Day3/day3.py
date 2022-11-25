try:
    import logging
    import os

except:
    print("Imports failed")

def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    for i,value in enumerate(input):
        input[i] = value.strip()
    

    return input

def split_binary(binary_nums):
    length = len(binary_nums[0])
    arr = []

    for i,value in enumerate(binary_nums):
        arr.insert(i, list(value))
    
    print(arr)
    return arr


def main():

    print(get_input())
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")