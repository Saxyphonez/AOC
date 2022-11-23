try:
    import logging
    import os
except:
    print("Imports failed")

#measurements = [199,200,208,210,200,207,240,269,260,263]

def get_input():
    input_filepath = os.getcwd() + "\\AOC\\2021\\Day1\\"+ "input.txt"

    with open(input_filepath,'r') as f:
        measurements = f.readlines()

    f.close()

    for i in range(len(measurements)):
        measurements[i] = int(measurements[i])

    return measurements

def main():
    increase_count = 0
    measurements = get_input()

    for i in range(len(measurements)):
        if i == 0:
            continue
        else:
            if measurements[i] > measurements[i-1]:
                increase_count += 1
            else:
                continue

    print("Number of increases: " + str(increase_count))



if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")


