try:
    import logging
    import os
    import sys

    # import re
    from utils import *

except ModuleNotFoundError or ImportError as e:
    print("Imports failed")
    print(e)

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
    for range_item in ranges_raw:
        ranges.append(Range_t(range_item))

    ingredients = []
    for item in ingredients_raw:
        ingredients.append(Ingredient_t(item))

    ranges.sort(key=lambda x:x.lower)
    combined_ranges = [] #where applicable

    for i, range_item in enumerate(ranges):

        if len(combined_ranges) == 0:
            combined_ranges.append(range_item)

        else:
            length_on_this_loop = len(combined_ranges)
            

            for i in range(length_on_this_loop):
                comparison_range = combined_ranges[i]

                if (range_item.lower < comparison_range.lower) and \
                    (range_item.upper < comparison_range.lower):
                    # range is outside (smaller end)
                    print("shouldnt happen?")
                    combined_ranges.append(range_item)


                elif (range_item.lower < comparison_range.lower) and \
                    (range_item.lower < comparison_range.upper) and \
                    (range_item.upper >= comparison_range.lower) and \
                    (range_item.upper <= comparison_range.upper):

                    # overlap (small side)
                    #print("{} <- {}overlap smaller".format(comparison_range, range_item))
                    comparison_range.lower = range_item.lower

                    #print("Comparison range now {}".format(comparison_range))
                    

                elif (range_item.lower >= comparison_range.lower) and \
                    (range_item.lower <= comparison_range.upper) and \
                    (range_item.upper >= comparison_range.lower) and \
                    (range_item.upper <= comparison_range.upper):

                    # total overlap 
                    #print("{} <- {} total overlap".format(comparison_range, range_item))
                    continue     

                elif (range_item.lower >= comparison_range.lower) and \
                    (range_item.lower <= comparison_range.upper) and\
                    (range_item.upper > comparison_range.upper):
                        
                    # overlap (bigger side)
                    #print("{} <- {} overlap bigger".format(comparison_range, range_item))
                    comparison_range.upper = range_item.upper

                    #print("Comparison range now {}".format(comparison_range))


                elif (range_item.lower > comparison_range.upper) and \
                    (range_item.upper > comparison_range.upper):

                    #range is outside (bigger end)
                    #print("{} <- {} Outside bigger".format(comparison_range, range_item))
                    if(i == length_on_this_loop-1):
                        #print("Extending combo list with {}".format(range_item))
                        #print()
                        combined_ranges.append(range_item)
                    else: 
                        continue
                
                else:
                    print("Not possible?")
                    print("{} <- {} size = {}".format(comparison_range, range_item, range_item.calc_valid_id_count()))
                    
                    #combined_ranges.append(range_item)
                
                    

    #print(combined_ranges)

    count = 0
    for item in combined_ranges:
        count += item.calc_valid_id_count()
    
    print("Count = {}".format(count))

    if TEST:
        #print("Valid ingredients = {}".format(valid_ids_set))
        # for item in ingredients:
        #     item.pretty_print()
        pass


    print("Done!")






if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
