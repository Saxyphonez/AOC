try:
    import logging
    import os
    import timeit

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

    input = [line.strip() for line in input]
    return input

def main():


    print("done")


if __name__ == "__main__":
    try:
        total_time = timeit.timeit('main', number=1, globals=globals())
        #main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    print('Average time: {} usec'.format((total_time/1)*1e6))