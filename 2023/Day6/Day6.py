try:
    import logging
    import os
    import timeit

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

    input = [line.strip() for line in input]
    return input

def parse(raw_input, line):
    buffer = raw_input[line].split()
    buffer.pop(0)
    buffer = [int(val) for val in buffer]

    return buffer


def get_combinations(time, max_distance, accln): #total time limit, current record distance, accln rate
    odd = None
    end_time = time - 1
    #max_time_held = 0

    suitable_times_held = []

    if (time+1) % 2 == 0: #even
        middle = ((time-3)/2) +1
        odd = False

    elif (time+1) % 2 == 1: #odd
        middle = (time-2)/2
        odd = True

    #print("time {} has middle {}".format(time, middle))

    for time_held in range(1, int(middle)+1):
        distance = time_held * accln * (time - time_held)

        if distance > max_distance:
            suitable_times_held.append(time_held)

        else:
            continue

    if not odd:
        num_combinations = 2 * len(suitable_times_held)
    else:
        num_combinations = (2 * len(suitable_times_held))+1

    return num_combinations
    # return (minimum_button time, maximum_button time, num_combos)


def main():
    raw_input = get_input()
    times = parse(raw_input, 0)
    distances = parse(raw_input, 1)

    combinations = []

    for i, time in enumerate(times):
        combinations.append(get_combinations(time, distances[i], 1))

    total = 1
    for i in combinations:
        total *= i

    print(total)
    print("done")   


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))