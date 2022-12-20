try:
    import logging
    import os
    from enum import Enum

except:
    print("Imports failed")

TEST = not True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Location():

    def __init__(self, name, x, y, height):
        self.name = name
        self.x = x
        self.y = y
        self.height = height

    def __repr__(self):
        return self.name

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def set_height(self, new_h):
        self.height = new_h

def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    input = [[y for y in x.strip()] for x in input]
    return input

def find_start_end(board):
    s_x = 0
    s_y = 0
    s_height = 'a'

    e_x = 0
    e_y = 0
    e_height = 'z'

    for y, row in enumerate(board):
        for x, col in enumerate(row):

            if col == 'S':
                s_x = x
                s_y = y
                board[y][x] = 'a'
            elif col == 'E':
                e_x = x
                e_y = y
                board[y][x] = 'z'
            else:
                continue
    
    start = Location('S', s_x, s_y, s_height)
    end = Location('E', e_x, e_y, e_height)
    return start, end

def calculate_move(board, cursor, w, h):
    x = cursor.x
    y = cursor.y
    curr_height = cursor.height
    neighbours = []

    try:
        neighbours.append(board[y-1][x]) #up

    except IndexError:
        neighbours.append(' ')

    try:
        neighbours.append(board[y+1][x]) #down

    except IndexError:
        neighbours.append(' ')

    try:
        neighbours.append(board[y][x-1]) #left

    except IndexError:
        neighbours.append(' ')

    try:
        neighbours.append(board[y][x+1]) #right

    except IndexError:
        neighbours.append(' ')

    possibles = []
    for i, val in enumerate(neighbours):
        if val == ' ':
            continue

        if ord(curr_height)-1 == ord(val) or ord(curr_height) == ord(val):
            if i == 0:
                possibles.append(Direction.UP)
                continue

            elif i == 1:
                possibles.append(Direction.DOWN)
                continue
            
            elif i == 2:
                possibles.append(Direction.LEFT)
                continue           

            elif i == 3:
                possibles.append(Direction.RIGHT)
                continue

    return possibles      

def move(cursor, dir):
    x = cursor.x
    y = cursor.y

    match dir:
        case Direction.UP:
            cursor.set_y(y-1)

        case Direction.DOWN:
            cursor.set_y(y+1)

        case Direction.LEFT:
            cursor.set_x(x-1)

        case Direction.RIGHT:
            cursor.set_x(x+1)

def update_moves(moves, x, y, dir, cursor):
    #THESE ARE ALL OPPOSITE BECAYSE I AM WOKRING FROM E TO S
    #RATHER THAN S TO E
    for test in dir:

        match test:
            case Direction.UP:
                if moves[y-1][x] == '.':
                    moves[y-1][x] = 'V'
                    move(cursor, test)
                    break
                else:
                    continue
            case Direction.DOWN:
                if moves[y+1][x] == '.':
                    moves[y+1][x] = '^'
                    move(cursor, test)
                    break
                else:
                    continue

            case Direction.LEFT:
                if moves[y][x-1] == '.':
                    moves[y][x-1] = '>'
                    move(cursor, test)
                    break
                else:
                    continue

            case Direction.RIGHT:
                if moves[y][x+1] == '.':
                    moves[y][x+1] = '<'
                    move(cursor, test)
                    break
                else:
                    continue

            case _:
                print("Toruble")
                break

def print_mov(moves):
    for y, row in enumerate(moves):
        for x, col in enumerate(row):
            print(col, end="")
        print(" ")

    print(" ")

def main():
    board = get_input()
    moves = []
    width = len(board[0])
    height = len(board)

    tmp = list(('.' for element in range(width)))

    for i in range(height):
        moves.append(tmp.copy())
    

    start, end = find_start_end(board)
    cursor = Location('C', end.x, end.y, end.height)
    moves[end.y][end.x] = 'E'
    #moves[start.y][start.x] = 'S'
    dir = []
    step_count = 0

    while not(cursor.x == start.x and cursor.y == start.y):
        dir.clear()

        dir = calculate_move(board, cursor, width, height).copy()#decide which way
        update_moves(moves, cursor.x, cursor.y, dir, cursor)#update the moves tracker (corrected for E to S travel)
        #move(cursor, dir)#update cursor position
        cursor.set_height(board[cursor.y][cursor.x])
        print_mov(moves)
        step_count+=1



    print(step_count)
    print("done")




if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")