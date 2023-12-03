try:
    import logging
    import os
    import re

except:
    print("Imports failed")

TEST =  not True

TEXT_NUMBERS = {
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9',
}

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


    pattern = re.compile(r"(?:(\d)|(?=(one|two|three|four|five|six|seven|eight|nine)))")
    #pattern = re.compile(r'\d')
    regex_numbers = re.findall(pattern, line)
    all_numbers= ["".join(x) for x in regex_numbers]
    #print(all_numbers) 

    for number in all_numbers:
            if number.isdigit():
                digits.append(number)
            else:
                digits.append(TEXT_NUMBERS[number])

    if len(digits) == 1:
        digits.append(digits[0])
    
    return digits[0]+digits[-1]



def main():
    input = get_input()

    important_digits = []
    for line in input:
        important_digits.append(get_digits(line))

    if TEST:
        print(important_digits)

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