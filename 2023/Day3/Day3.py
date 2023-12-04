try:
    import logging
    import os
    import re

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
        self.symbols = {}


        self.parse_input(sch_txt)
        


    def parse_input(self, text):
        symbol_buffer = []
        for i, line in enumerate(text):
            symbol_buffer.clear()
            self.board.append(line)

            #use regex to find symbols
            pattern = re.compile(r"(?:[^\.0-9\n])")

            #for each symbol, get x and y and type
            for match in re.finditer(pattern, line):
                symbol_buffer.append(self.record_symbol(match_obj= match, line = i+1))
            
            #append to big dict of symbols (list of symbols - value) on a line (key)
            if len(symbol_buffer) > 0:
                self.symbols[i+1] = symbol_buffer.copy()
            

    def record_symbol(self, match_obj, line):
        # print(match_obj.group())
        # print(line)
        symbol = Symbol(symbol = match_obj.group(),
                        x = match_obj.start(),
                        y = line)

        return symbol

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
    input = get_input()
    schematic = Schematic(input)

    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")