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

    m_pos = [] #[[row,col]]

    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == "M":
                buf = [r,c]
                m_pos.append(buf)
            else:
                continue
    #m_pos = []  
    a_pos = [] 
    s_pos = []
   
    total = 0
    for coord in m_pos:
        # r = coord[0]
        # c = coord[1]
        total += check_neighbours(board, coord, width, length)


    
    print(total/2)
    print("Done!")


def check_neighbours(board, coord, width, length):
    r, c = coord[0], coord[1] #get row and column

    #check 3x3 around this:

    #get possibilites of positions including edge cases:
    up = True if r-2>=0 else False
    down = True if r+2<=width-1 else False
    left = True if c-2>=0 else False
    right = True if c+2<=length-1 else False

    UL = up and left
    UR = up and right
    DL = down and left
    DR = down and right

    valid_dirs = [up, down, left, right, UL, UR, DL, DR]

    num_of_xmas = 0
    for i, dir in enumerate(valid_dirs):
        if i<=3:
            continue
        elif dir == True:
            if(check_dirn(board, r, c, i)):
                #check_cross(board, r,c,i)
                #print("!M@  R:{} C:{}".format(r, c))
                num_of_xmas +=1
            else:
                continue
        else:
            continue

    return num_of_xmas
   
def check_dirn(board, row, col, dirn_id):
    buf = []
    match dirn_id:
        case 0: #up
            for i in range(2):
                buf.append(board[row-1-i][col])
            pass            
        case 1: #down
            for i in range(2):
                buf.append(board[row+1+i][col]) 

        case 2: #left
            for i in range(2):
                buf.append(board[row][col-1-i]) 
           
        case 3: #right
            for i in range(2):
                buf.append(board[row][col+1+i]) 
            pass

        case 4: #up and left
            for i in range(2):
                buf.append(board[row-1-i][col-1-i])

        case 5: #up and right
            for i in range(2):
                buf.append(board[row-1-i][col+1+i])

        case 6: #down and left
            for i in range(2):
                buf.append(board[row+1+i][col-1-i])

        case 7: #down and right
            for i in range(2):
                buf.append(board[row+1+i][col+1+i])

        case _:
            print("bad state")

    if(''.join(buf)=="AS"):
        print("AS")
        if(check_cross(board, row, col, dirn_id)):
            #print("Cross")
            return True
        else:
            return False
    else:
        return False


def check_cross(board, row, col, mas_dir):
    #opposites:
    #UL is DR
    #UR is DL
    #DL is UR
    #DR is UL

    match (mas_dir):
        case 4: #up and left
            #print("UL")
            row_corner = col - 2
            col_corner = row - 2

        case 5: #up and right
            #print("UR")
            row_corner = col + 2
            col_corner = row - 2
                          

        case 6: #down and left
            #print("DL")
            row_corner = col - 2
            col_corner = row + 2
                         

        case 7: #down and right
            # print("DR")
            row_corner = col + 2
            col_corner = row + 2
            
        case _:
            print("bad state2")

    corner_one = board[row][row_corner]
    corner_two = board[col_corner][col]
    #print("M@  R:{} C:{}".format(row, col))
    #print("corner1 {}({},{})    corner2 {}({},{})".format(corner_one,row, row_corner, corner_two,col_corner,col))

    if(corner_one=="M" and corner_two=="S") or (corner_one=="S" and corner_two=="M"):
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
