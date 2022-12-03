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

    for i, value in enumerate(input):
        input[i] = value.strip()

    return input

def badge(backpacks):
    separated =[]

    for i, val in enumerate(backpacks):
        separated.append(set(val))

    com_item_tmp = list(set(separated[0]).intersection(separated[1]))
    com_item = list(set(com_item_tmp).intersection(separated[2]))
    return com_item


def get_priority(letter):
    priority = None
    if letter.isupper():
        priority =  ord(letter) - 38

    elif letter.islower():
        priority =  ord(letter) - 96

    else:
        logging.error("cant tell what letter is")
    return priority

def main():
    input = get_input()
    common_items = []
    iterations_needed = int(len(input)/3)

    for i in range(iterations_needed):
        common_items.extend(badge(input[3*i:(3*i)+3]))

    #print(common_items)
    score = 0
    #score = []

    for item in common_items:
        score += get_priority(item)
        #score.append(get_priority(item))

    print(score)
    #print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")