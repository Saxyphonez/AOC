try:
    import logging
    import os
    import sys

    # import re

except ModuleNotFoundError or ImportError as e:
    print("Imports failed")
    print(e)

TEST = not True

CHAR_LIST = list("MAS")

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

    input = [line.strip() for line in input]
    return input

def main():

    print("Test is {}".format(TEST))
    input = get_input()

    board = [list(x) for x in input]
    width = len(board[0])
    length = len(board)


    #get a list of positions for all the x's
    #iterate through that list and find neighbouring m's
    #iterate through that list and find neighbouring s's
    #iterate through that list and find neighbouring s's

    x_pos = [] #[[row,col]]

    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == "X":
                buf = [r,c]
                x_pos.append(buf)
            else:
                continue
    m_pos = []  
    a_pos = [] 
    s_pos = []
   
    total = 0
    for coord in x_pos:
        # r = coord[0]
        # c = coord[1]
        total += check_neighbours(board, coord, width, length)


    
    print(total)
    print("Done!")


def check_neighbours(board, coord, width, length):
    r, c = coord[0], coord[1] #get row and column

    #check 3x3 around this:

    #get possibilites of positions including edge cases:
    up = True if r-3>=0 else False
    down = True if r+3<=width-1 else False
    left = True if c-3>=0 else False
    right = True if c+3<=length-1 else False

    UL = up and left
    UR = up and right
    DL = down and left
    DR = down and right

    valid_dirs = [up, down, left, right, UL, UR, DL, DR]

    num_of_xmas = 0
    for i, dir in enumerate(valid_dirs):
        if dir == True:
            if(check_dirn(board, r, c, i)):
                num_of_xmas+=1
            else:
                continue
        else:
            continue

    return num_of_xmas
   
def check_dirn(board, row, col, dirn_id):
    buf = []
    match dirn_id:
        case 0: #up
            for i in range(3):
                buf.append(board[row-1-i][col]) # +1 because we start on an "X"
            pass            
        case 1: #down
            for i in range(3):
                buf.append(board[row+1+i][col]) 

        case 2: #left
            for i in range(3):
                buf.append(board[row][col-1-i]) 
           
        case 3: #right
            for i in range(3):
                buf.append(board[row][col+1+i]) 
            pass

        case 4: #up and left
            for i in range(3):
                buf.append(board[row-1-i][col-1-i])

        case 5: #up and right
            for i in range(3):
                buf.append(board[row-1-i][col+1+i])

        case 6: #down and left
            for i in range(3):
                buf.append(board[row+1+i][col-1-i])

        case 7: #down and right
            for i in range(3):
                buf.append(board[row+1+i][col+1+i])

        case _:
            print("bad state")

    if(''.join(buf)=="MAS"):
        return True
    else:
        return False

            
def clean_board(x_pos, m_pos, a_pos, s_pos, width, length):
    #generate board with . for irrelevant
    buf = []
    for i in range (width):
        buf.append(".")

    cleaned = []
    for i in range(length):
        cleaned.append(buf.copy())
   
    for coord in x_pos:
        cleaned[coord[0]][coord[1]] = "X"
    
    for coord in m_pos:
        cleaned[coord[0]][coord[1]] = "M"

    for coord in a_pos:
            cleaned[coord[0]][coord[1]] = "A"

    for coord in s_pos:
            cleaned[coord[0]][coord[1]] = "S"

    cleaned = [[''.join(x)+"\n"] for x in cleaned]
    
    with open('test_output.txt','w') as f:
        for line in cleaned:
            f.writelines(line)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
