try:
    import logging
    import os
    from enum import Enum

except:
    print("Imports failed")

TEST = True

class NextMove(Enum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2
    NOTHING = 4

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 4

class Cart:

    #Class variables
    next_move = NextMove.NOTHING #for intersections
    previous_move = NextMove.NOTHING

    current_direction = None

    def __init__(self, direction, x, y):
        self.current_direction = direction
        self.x= x #starting state
        self.y = y

    def calculate_next_move(self):
        #set next move here 
        #move current move to previous move
        pass

    def set_location(self, x, y):
        pass

    def get_location(self, x, y):
        return self.x, self.y #where am I rn

    def next_direction(self ):
        #for intersections
        pass

    def turn_corner(self, which_way):
        #for turning the corner
        pass


if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    #return input

def main():


    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")