try:
    import logging
    import os

except:
    print("Imports failed")

TEST = True
BOARD_L = 21
BOARD_W = 26

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
            if new_y < BOARD_W or new_y >=0:
                h_obj.set_y(new_y)


        case 'D':
            new_y = h_obj.get_y() - 1
            if new_y < BOARD_W or new_y >=0:
                h_obj.set_y(new_y)


        case 'L':
            new_x = h_obj.get_x() - 1
            if new_x < BOARD_L or new_x >=0:
                h_obj.set_x(new_x)


        case 'R':
            new_x = h_obj.get_x() + 1
            if new_x < BOARD_L or new_x >=0:
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

    x_diff = h_x - t_x
    y_diff = h_y - t_y

    #figure out move here:
    #do the moves as + and - 
    if abs(x_diff) ==2 and abs(y_diff) == 0: #L/R
        if x_diff > 0:
            move_t(t_obj, 1, 0)
        elif x_diff < 0:
            move_t(t_obj, -1, 0)

    elif abs(y_diff) ==2 and abs(x_diff) == 0: #U/D
        if y_diff > 0:
            move_t(t_obj, 0, 1)
        elif y_diff < 0:
            move_t(t_obj, 0, -1)

    else:
        if (x_diff == -1 and y_diff == 2) or (x_diff == -2 and y_diff == 1):
            #move left and up
            move_t(t_obj, -1, 1)
        elif (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1):
            #move right and up
            move_t(t_obj, 1, 1)
        elif (x_diff == 1 and y_diff == -2) or (x_diff == 2 and y_diff == -1):
            #move right and down
            move_t(t_obj, 1, -1)
        elif (x_diff == -1 and y_diff == -2) or (x_diff == -2 and y_diff == -1):
            #move left and down
            move_t(t_obj, -1, -1)

    #update board:
    if t_obj.name == '9':
        try:
            board[(BOARD_L - 1) - t_obj.get_y()][t_obj.get_x()] += 1
        except IndexError:
            print(str(t_obj.get_y()) + " "  + str(t_obj.get_x()))


def is_touching(h_obj, t_obj):
    #figure out
    x_diff = abs(h_obj.get_x() - t_obj.get_x())
    y_diff = abs(h_obj.get_y() - t_obj.get_y())

    if (x_diff <=1 and y_diff<=1) or (x_diff == 1 and y_diff == 1):
        return True

    else:
        return False

def main():

    ropes = []
    for i in range(10):
        if i == 0:
           ropes.append(RopeEnd("H", 0,0))
           continue

        else:   
            ropes.append(RopeEnd(str(i), 0,0))


    moves = get_input()


    board = []
    tmp = list((0 for element in range(BOARD_W)))

    for i in range(BOARD_L):
        board.append(tmp.copy())

    board[BOARD_L-1 - ropes[9].get_y()][ropes[9].get_x()] = 1 



    for i, instruction in enumerate(moves):
        repeats = int(instruction[1])

        for j in range(repeats):
            move_h(instruction, ropes[0])

            for k, rope_obj in enumerate(ropes):
                if k == 9:
                    break
                else:
                    if not is_touching(rope_obj,ropes[k+1]):
                        #calculate tail move and then move it
                        calculate_tail_move(rope_obj, ropes[k+1], board)


    num_visited_positions = 0
    for i, row in enumerate(board):
        for j, pos in enumerate(row):
            if pos >= 1:
                num_visited_positions += 1
            else:
                continue
    
    print(num_visited_positions)
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")