try:
    import logging
    import os
    import pandas as pd

except:
    print("Imports failed")

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
    input = [list(x.strip()) for x in input]
    df = pd.DataFrame(list(input))
    return df

def main():
    df_input = get_input()
    print(df_input.values)

    perimeter = ((2*df_input.shape[0]) + 2*(df_input.shape[1]-2))
    print(perimeter)
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")