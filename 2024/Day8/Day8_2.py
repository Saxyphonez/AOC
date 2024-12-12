try:
    import logging
    import os
    import sys

    import re

except ModuleNotFoundError or ImportError as e:
    print("Imports failed")
    print(e)

TEST = not True

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
    length = len(board)
    width = len(board[0])


    antenna_map = find_antennae(board=board)
    antinode_map = {}

    for freq, coords in antenna_map.items():
        antinode_map[freq] = find_antinodes(freq, coords, length, width)


    unique_points = set()

    for key, values in antinode_map.items():
        for val in values:
            unique_points.add(val)

    print(len(unique_points))
    print("Done!")


def find_antinodes(freq, coords, length, width):
    #matrix = []
    antinodes = []
    combo_checked = []
    for r in range (len(coords)):
        buf = []

        for c in range(len(coords)):
            if r==c:
                buf.append(0)
                continue
            else:
                #buf.append(diff_vector(coords[r],coords[c]))
                if (coords[r],coords[c]) in combo_checked or (coords[c],coords[r]) in combo_checked:
                    continue
                else:
                    antinodes.extend(get_antinodes_on_line(coords[r],coords[c], length, width))
                    combo_checked.append((coords[r],coords[c]))


        #matrix.append(buf)

    # antinodes = []

    # for i, line in enumerate(matrix):
    #     for dif in line:

    #         if dif == 0:
    #             continue
    #         else:
    #             new_row, new_column = apply_diff_vector(coords[i], dif)

    #             if check_onboard(new_row, new_column, length, width):
    #                 antinodes.append((new_row, new_column))

    return antinodes


def get_antinodes_on_line(point_one, point_two, length, width):
    #bsaically use y-y1 = m(x-x1)   where y is row and x is column
    vector = diff_vector(point_one, point_two)
    row_one = point_one[0]
    column_one = point_one[1]

    m = vector[0]/vector[1]


    antinodes = []
    for col in range(width):
        row = (m*(col-column_one)) + row_one

        if check_onboard(row, col, length, width):
            if (row.is_integer()):
                antinodes.append((int(row),col))
        else:
            continue


    return antinodes



def check_onboard(row, col, length, width):
    if (row>=0) and (row<length) \
        and (col>=0) and (col<width):
        
        return True
    
    else:
        return False


def apply_diff_vector(coord, vector):
    new_row = coord[0] + (-1* vector [0])
    new_column = coord[1] + (-1* vector [1])

    return new_row, new_column



def diff_vector(start, finish):

    diff_row = finish[0] - start[0]
    diff_column = finish[1] - start[1]

    return (diff_row, diff_column)


def find_antennae(board):
    antenna_map = {}
    for row, line in enumerate(board):
        for column, val in enumerate(line):

            if re.match(r'[A-Za-z]|[0-9]', val): #is alphanumeric
                if val in antenna_map.keys():
                    antenna_map[val].append((row, column))
                else:
                    antenna_map[val] = [(row,column)]

    return antenna_map


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
