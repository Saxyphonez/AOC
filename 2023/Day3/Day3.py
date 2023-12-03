try:
    import logging
    import os

except:
    print("Imports failed")

TEST = True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"


class Schematic:
#TODO regex to find numbers in the line. Add that to a dict
#TODO get coords of each

    def __init__(self, sch_txt):
       
        self.board = []#[y coord(inc as you go down)][x coord ]

        self.parse_input(sch_txt)
        self.symbols = []


    def parse_input(self, text):
        for i, line in enumerate(text):
                self.board.append(line)

                #use regex to find symbols
                #for each symbol, get x and y and type
                #append to big list of symbols



    def __repr__(self):
        str = "TODO rpr"
        return(str)
    
    def __str__(self):
        str = "TODO str"
        return str


class Symbol:
    def __init__(self, symbol, x, y):
        self.x = x
        self.y = y
        self.name = symbol

    def __repr__(self):
        str = "{} (Y{}:,X:{})".format(self.name, self.y, self.x)
        return(str)
    
    def __str__(self):
        str = "{} (Y{}:,X:{})".format(self.name, self.y, self.x)
        return(str)


def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    input = [line.strip() for line in input]
    return input

def main():


    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")