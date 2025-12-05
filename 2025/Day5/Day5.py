try:
    import logging
    import os
    import sys

    # import re
    from utils import *

except ModuleNotFoundError or ImportError as e:
    print("Imports failed")
    print(e)

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


def parse_input(input):
    #split on newline
    newline_idx = input.index("")

    ranges = input[:newline_idx]
    ingredients = input[newline_idx+1:]

    ingredients = [int(x) for x in ingredients]

    return ranges, ingredients


def main():

    print("Test is {}".format(TEST))
    input = get_input()

    ranges_raw, ingredients_raw = parse_input(input)

    ranges = []
    for range in ranges_raw:
        ranges.append(Range_t(range))

    ingredients = []
    for item in ingredients_raw:
        ingredients.append(Ingredient_t(item))


    count = 0

    for i, ingredient in enumerate(ingredients):
        for range in ranges:
            if range.in_range(ingredient.id):

                if ingredient.range_count == 0:
                    ingredient.set_state(IngredientStatus.FRESH)
                    count +=1

                ingredient.add_range(range)
                
            else:
                if ingredient.state != IngredientStatus.FRESH:
                    ingredient.set_state(IngredientStatus.SPOILT)
                continue

    print("Count = {}".format(count))

    if TEST:
        for item in ingredients:
            item.pretty_print()


    print("Done!")






if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
