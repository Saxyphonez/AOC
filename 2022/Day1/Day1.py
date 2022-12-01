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
    buffer = []
    output =[]

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()
            
    for i, value in enumerate(input):
        if value == '\n':
            output.append(buffer.copy())
            buffer.clear()
        else:
            num = int(value.strip())
            buffer.append(num)

    output.append(list(buffer))
    print(output)
    return output

def main():
    each_elf = get_input()
    calories = []

    for i, calories_list in enumerate(each_elf):
        total_for_elf = sum(calories_list)
        calories.append(total_for_elf)

    #print(calories)
    max_value = max(calories)
    index = calories.index(max_value)

    print(index)
    print(max_value)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
