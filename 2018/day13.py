try:
    import logging
    import os
    from enum import Enum
    import pandas as pd
    import numpy as np

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

class Track_Direction(Enum):
    UD = 0
    LR = 1
    BEND_L = 2
    BEND_R = 3

class Track_Type(Enum):
    STRAIGHT = 0
    CURVE = 1
    INTERSECTION = 2

class Track:
    track_type = None
    track_bend = None

    def __init__(self, track_type, x, y):
        self.track_type = track_type
        self.x = x #starting state
        self.y = y

    def bend_direction(self, surrounding_tracks):
        pass


#def find_carts:

if TEST:
    input_filename = "test_input_full.txt"
else:
    input_filename = "input.txt"

def get_input():
    input = []
    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)

    with open(input_filepath,'r') as f:
        input = f.read().splitlines()

    indiv = []
    for i, val in enumerate(input):

        indiv.append(list(val))

    df = pd.DataFrame(indiv)
    return df

def parse_start(board_start):
    x_lim, y_lim = board_start.shape
    carts = []
    board = []

    for x in range(x_lim) : #x across, y down
        for y in range(y_lim):
            item = board_start.iloc[(x,y)]

           # if item == 'v' or item == '^' or item == '<' or item == '>':
            #based on item
            #else:
                

def main():
    df_board_input = get_input()
    #parse_start(df_board_input)


    print(df_board_input)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")