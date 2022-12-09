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

    def set_x(self, new_x):
        self.x = new_x

    def get_x(self):
        return self.x

    def set_y(self, new_y):
        self.y = new_y

    def get_y(self):
        return self.y

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


def move_h(move, h_obj):
    dir = move[0]

    #NOTE: going along cols is the x axis, going down rows is y axis
    match dir:
        case 'U':
            new_y = h_obj.get_y() + 1
            h_obj.set_y(new_y)


        case 'D':
            new_y = h_obj.get_y() - 1
            h_obj.set_y(new_y)


        case 'L':
            new_x = h_obj.get_x() - 1
            h_obj.set_x(new_x)


        case 'R':
            new_x = h_obj.get_x() + 1
            h_obj.set_x(new_x)
            

def move_t(t_obj, x_move, y_move):
    new_y = t_obj.get_y() + y_move
    new_x = t_obj.get_x() + x_move

    #NOTE: going along cols is the x axis, going down rows is y axis
    t_obj.set_x(new_x)
    t_obj.set_y(new_y)


def calculate_tail_move(h_obj, t_obj, board):
    h_x = h_obj.get_x()
    h_y = h_obj.get_y()

    t_x = t_obj.get_x()
    t_y = t_obj.get_y()

    x_move = 0
    y_move = 0

    #figure out move here:
    #do the moves as + and - 
    #if x_diff >=2 #L/R
    #if y_diff >=2 #U/D
    #if (ABC):
        #move diagonal

    #move the tail
    move_t(t_obj, x_move, y_move)

    #update board:
    board[t_obj.get_y()][t_obj.get_x()] += 1 

def is_touching(h_obj, t_obj):
    #figure out
    x_diff = abs(h_obj.get_x() - t_obj.get_x())
    y_diff = abs(h_obj.get_y() - t_obj.get_y())

    if (x_diff <=1 and y_diff<=1) or (x_diff ==1 and y_diff ==1):
        return True

    else:
        return False

def main():
    head = RopeEnd("H", 0, 0)
    tail = RopeEnd("T", 0, 0)
    board = []
    moves = get_input()

    tmp = list((0 for element in range(BOARD_W)))
    for i in range(BOARD_L):
        board.append(tmp.copy())

    board[BOARD_L-1][0] = 1 
    

    for i, instruction in enumerate(moves):
        repeats = int(instruction[1])

        for j in range(repeats):
            move_h(instruction, head)

            if is_touching(head,tail):
                continue
            else:
                calculate_tail_move(head, tail, board)
    
    

    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")