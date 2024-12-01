try:
    import logging
    import os
    import sys

    # import re

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

def main():

    print("Test is {}".format(TEST))
    input = get_input()

    reports = [x.split(" ") for x in input]
    reports = [list(map(int, x)) for x in reports]


    report_safety_status = []

    for report in reports:
        report_safety_status.append(check_safety(report))

    print("Pre damp {}".format(report_safety_status))

    count = 0
    for status in report_safety_status:
        if(status):
            count+=1

    print("Safe rerpot count: {}".format(count))




    for i, status in enumerate(report_safety_status):
        if(problem_damping(reports[i])):
            report_safety_status[i] = True
        else:
            continue

    print("Post damp {}".format(report_safety_status))   

    count = 0
    for status in report_safety_status:
        if(status):
            count+=1
    print("Safe rerpot count (damped): {}".format(count))

    print("Done!")

def problem_damping(report):
    #False - still unsafe
    #True - damping makes it sage

    is_safe = False

    for i, item in enumerate(report):
        modified = report.copy()
        modified.pop(i)

        if(check_safety(modified)):
            is_safe = True

    return is_safe

def check_safety(report):
    #False is unsafe
    #True is safe

    #check ascending
    #check a step is between 1 and 3 inclusiveely
    previous_level = 0
    ascending = None # we think it is ascending based on the first 2 numbers
    descending = None # we think it is descending based on the first 2 numbers

    for i, level in enumerate(report):
        if i == 0:
            previous_level = level
            continue

        else:
            difference = level - previous_level
            diff_abs = abs(difference)
            previous_level = level

            if difference < 0:
                if(ascending): # if the step is decreasing but we think we should be ascending. That's bad
                    return False
                
                if(descending is None):# if we dont know yet, set descending as the step is in the downward direction
                    descending = True

                if (descending):
                    if(diff_abs>=1 and diff_abs <=3):
                        continue # Continue through the list
                    else:
                        return False # Unsafe condition

                elif (ascending):
                    return False
                    
                    

            elif difference > 0:
                if(descending): # if the step is increasing but we think we should be descending. That's bad
                    return False
                
                if(ascending is None): # if we dont know yet, set ascending as the step is in the upward direction
                    ascending = True

                if(ascending):
                    if(diff_abs>=1 and diff_abs <=3):
                        continue # Continue through the list
                    else:
                        return False # Unsafe condition
                


            elif difference == 0:
                return False

    # Went through the whole list and did not hit a return False#
    # So must be safe and return True
    return True 



if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
