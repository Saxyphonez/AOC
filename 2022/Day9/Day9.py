try:
    import logging
    import os

except:
    print("Imports failed")

TEST = True
BOARD_L = 10
BOARD_W = 10
"""
input parsing for the moves

func for tail next move

func for move execution

rope_end class:
    name string
    x,y locations

2d array for the board
"""

class RopeEnd():


    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return str(self.name)


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

    input = [x.strip().split(" ") for x in input] 
    return input

def main():
    head = RopeEnd("H", 0, 0)
    tail = RopeEnd("T", 0, 0)
    board = []
    moves = get_input()

    tmp = list((0 for element in range(BOARD_W)))
    for i in range(BOARD_L):
        board.append(tmp.copy())

    board[BOARD_L-1][0] = 1 
    """
    for i, move in enumerate(moves):
        move head()
        calculate & do move tail()
            update board with tail visits()
    
    """

    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")