try:
    import logging
    import os
    from enum import Enum
    import pandas as pd
    import numpy as np

    from prints import *

except:
    print("Imports failed")

TEST = True

class NextMove(Enum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2
    NOTHING = 4

class Cart_Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 4

class Track_Direction(Enum):
    UD = 0
    LR = 1
    BEND_L = 2
    BEND_R = 3

class Track_Type(Enum):
    STRAIGHT = 0
    CURVE = 1
    INTERSECTION = 2
    EMPTY = 3

class Cart:

    #Class variables
    next_move = NextMove.NOTHING #for intersections
    previous_move = NextMove.NOTHING
    cart_string = None
    current_direction = None

    def __init__(self, direction, x, y):
        self.current_direction = direction
        self.x= x #starting state
        self.y = y
        self.cart_string = self.set_cart_string(self.current_direction)#set the string to print

    def set_cart_string(self, direction):
        match direction:
            case Cart_Direction.UP:
                #self.cart_string = '^'
                return '^'

            case Cart_Direction.DOWN:
                #self.cart_string = 'v'
                return 'v'
            case Cart_Direction.LEFT:
                #self.cart_string = '<'
                return '<'

            case Cart_Direction.RIGHT:
                #self.cart_string = '>'
                return '>'
                
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

class Track:
    track_type = None
    track_bend = None
    track_string = None

    def __init__(self, track_type, x, y, track_string):
        self.track_type = track_type
        self.x = x #starting state
        self.y = y
        self.track_string = track_string

    def bend_direction(self, surrounding_tracks):
        pass


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


def get_direction_of_cart(item):
    match item:

        case 'v':
            return Cart_Direction.DOWN
        
        case '^':
            return Cart_Direction.UP

        case '<':
            return Cart_Direction.LEFT

        case '>':
            return Cart_Direction.RIGHT


def get_track_type(item):
    match item:

        case '|':
            return Track_Type.STRAIGHT
        
        case '-':
            return Track_Type.STRAIGHT

        case '\\':
            return Track_Type.CURVE

        case '/':
            return Track_Type.CURVE

        case '+':
            return Track_Type.INTERSECTION


def parse_start(board_start):
    x_lim, y_lim = board_start.shape
    df_cart_map = pd.DataFrame(index=range(x_lim),columns=range(y_lim))
    df_track_map = df = pd.DataFrame(index=range(x_lim),columns=range(y_lim))


    for x in range(x_lim) : #x across, y down
        for y in range(y_lim):
            item = board_start.iloc[(x,y)]

            if item == ' ':
                track = Track(track_type= Track_Type.EMPTY,
                                x=x, 
                                y=y,
                                track_string=' ')
                df_track_map.iloc[(x,y)] = track
                df_cart_map.iloc[(x,y)] = ' ' 
                continue

            elif item == 'v' or item == '^' or item == '<' or item == '>':
                cart = Cart(direction=get_direction_of_cart(item), 
                            x=x, 
                            y=y)
                df_cart_map.iloc[(x,y)] = cart

                if cart.current_direction == Cart_Direction.UP or cart.current_direction == Cart_Direction.DOWN:
                    underlaying_track_dir = Track_Direction.UD
                    track_string = '|'

                elif cart.current_direction == Cart_Direction.LEFT or cart.current_direction == Cart_Direction.RIGHT:
                    underlaying_track_dir = Track_Direction.LR
                    track_string = '-'
                
                df_track_map.iloc[(x,y)] = Track(track_type = underlaying_track_dir,
                                            track_string = track_string,
                                            x=x, 
                                            y=y)

            elif item == '\\' or item == '/' or item == '-' or item == '|' or item == '+':
                track = Track(track_type= get_track_type(item),
                            x=x, 
                            y=y,
                            track_string=item)
                df_track_map.iloc[(x,y)] = track
                df_cart_map.iloc[(x,y)] = ' ' 
            else:
                logging.error("cant tell what this item is")
                exit()


    print_track(df_track_map)
    print(df_cart_map)
    return df_track_map, df_cart_map
                
#def find_carts:


def main():
    df_board_input = get_input()
    print(df_board_input)
    df_track_map, df_cart_map = parse_start(df_board_input) #the cart map overlays on track map


    #print(df_board_input)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")