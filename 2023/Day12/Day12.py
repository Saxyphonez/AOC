try:
    import logging
    import os
    import timeit
    import re

except:
    print("Imports failed")

TEST = True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

class ClassName:
    def __init__(self ):
        self.name = "TODO"
        pass


    def __repr__(self):
        str = "{}".format(self.name)
        return(str)
    
    def __str__(self):
        return(self.__repr__())
    

def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    input = [line.strip() for line in input]
    input = [line.split(" ") for line in input]

    #input = [[list(line[0]), line[1].split(",")] for line in input]
    input = [[line[0], line[1].split(",")] for line in input]
    return input

def main():
    input = get_input()
    print(input)

    print("done")


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))