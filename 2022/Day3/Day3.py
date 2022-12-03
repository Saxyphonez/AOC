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

    return input

def common_item(backpack):
    length = len(backpack)
    halfway = int((length)/2)
    backpack_list = list(backpack)

    first_half = backpack_list[0:halfway]
    second_half = backpack_list[halfway:]
    com_item = list(set(first_half).intersection(second_half))

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

    for i, value in enumerate(input):
        common_items.extend(common_item(value.strip()))

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