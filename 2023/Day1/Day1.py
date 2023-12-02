try:
    import logging
    import os

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

def get_digits(line):
    digits = []

    for char in list(line):
        if char.isdigit():
            digits.append(char)
        else:
            continue

    if len(digits) == 1:
        digits.append(digits[0])
    
    return digits[0]+digits[-1]



def main():
    input = get_input()

    important_digits = []
    for line in input:
        important_digits.append(get_digits(line))

    #print(important_digits)
    total = 0
    for number in important_digits:
        total+= int(number)

    print(total)
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")