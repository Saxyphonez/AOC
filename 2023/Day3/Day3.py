try:
    import logging
    import os
    import re

except:
    print("Imports failed")

TEST = not True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"


class Schematic:

    def __init__(self, sch_txt):
       
        self.board = []#[y coord(inc as you go down)][x coord ]
        self.symbols = []
        self.numbers = []

        self.parse_input(sch_txt)
        


    def parse_input(self, text):
        symbol_buffer = []
        number_buffer = []

        pattern_sym = re.compile(r"(?:[^\.0-9\n])")
        pattern_num = re.compile(r"(?:[0-9]+)")

        for i, line in enumerate(text):
            symbol_buffer.clear()
            number_buffer.clear()

            self.board.append(line)
    
            #use regex to find symbols
            
            for match_sym in re.finditer(pattern_sym, line):
                symbol_buffer.append(self.record_symbol(match_obj= match_sym, line = i+1))

            if len(symbol_buffer) > 0:
                self.symbols.extend(symbol_buffer.copy())

            #use regex to find numbers
           
            for match_num in re.finditer(pattern_num, line):
                number_buffer.append(self.record_number(match_obj= match_num, line = i+1))

            if len(number_buffer) > 0:
                self.numbers.extend(number_buffer.copy())

            



    def record_symbol(self, match_obj, line):
        symbol = Symbol(symbol = match_obj.group(),
                        x = match_obj.start(),
                        y = line)

        return symbol
    
    def record_number(self, match_obj, line):
        number = Number(number = match_obj.group(),
                        x = match_obj.span(),
                        y = line)

        return number

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
        str = "{} (Y:{},X:{})".format(self.name, self.y, self.x)
        return(str)
    
    def __str__(self):
        str = "{} (Y:{},X:{})".format(self.name, self.y, self.x)
        return(str)


class Number:
    def __init__(self, number, x, y):
        self.x_pos = [x[0], x[1]]
        self.y = y
        self.num = str(number)
        self.is_part = False

    def __repr__(self):
        str = "{} (Y:{},X:{})".format(self.num, self.y, self.x_pos)
        return(str)
    
    def __str__(self):
        str = "{} (Y:{},X:{})".format(self.num, self.y, self.x_pos)
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

    for symbol in schematic.symbols:
        sym_x = symbol.x
        sym_y = symbol.y
        sym_x_range = {sym_x-1, sym_x, sym_x+1}

        for number in schematic.numbers:
            num_x = {*range(number.x_pos[0], number.x_pos[1])}
            num_y = number.y

            if ((num_y == sym_y-1) and (sym_x_range.intersection(num_x))):
                number.is_part = True

            elif ((num_y == sym_y) and (sym_x_range.intersection(num_x))):
                number.is_part = True

            elif((num_y == sym_y+1) and (sym_x_range.intersection(num_x))):
                number.is_part = True
            else:
                #print("{} not part for symbol [{}]".format(number.num, symbol))
                pass

    total = 0
    for number in schematic.numbers:
        if number.is_part:
            total+=int(number.num)
    print(total)
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")