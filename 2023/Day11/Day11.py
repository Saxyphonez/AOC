try:
    import logging
    import os
    import timeit
    import re

except:
    print("Imports failed")

TEST = not True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

    
class Galaxy:
    def __init__(self, name, col, row ):
        self.name = str(name)
        self.col = col
        self.row = row
        pass


    def __repr__(self):
        str = "Gal:{} Row: {}, Col:{}".format(self.name, self.row, self.col)
        return(str)
    
    def __str__(self):
        return(self.__repr__())
    

def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    input = [line.strip() for line in input]
    return input

def galaxy_parse(raw_input):
    galaxy_list = []
    count = 0
    for i, line in enumerate(raw_input):

        for j, col in enumerate(line):
            if col == "#":
                galaxy_list.append(Galaxy(name = count+1, col = j, row = i))
                count += 1
            else:
                continue

    return galaxy_list

def dist_getter(galaxies):
    all_dist = []

    for i, src_gal in enumerate(galaxies):
        tmp_dist = []

        for dest_gal in galaxies[i+1:]:
        # for dest_gal in galaxies[i+1:]:
            row_diff = abs(dest_gal.row - src_gal.row)
            col_diff = abs(dest_gal.col - src_gal.col)
            dist = row_diff + col_diff

            tmp_dist.append(dist)

        all_dist.append(tmp_dist)

    return all_dist


def galaxy_adjuster(galaxies, blank_rows, blank_cols):
    galaxies_list = galaxies.copy()
    #big list of galaxies
    # go through each
    # For gal.col, see how many blank rows exist <gal.col
    #add that many to gal.col
    #repeat for gal.row

    for galaxy in galaxies_list:
        col_orig = galaxy.col
        row_orig = galaxy.row

        row_adjust = 0
        col_adjust = 0

        for blank_row in blank_rows:
            if blank_row < row_orig:
                row_adjust += 1
            else:
                continue

        for blank_col in blank_cols:
            if blank_col < col_orig:
                col_adjust += 1
            else:
                continue
        
        galaxy.col += col_adjust
        galaxy.row += row_adjust

    return galaxies_list

def main():
    raw_input = get_input()

    board = []
    for line in raw_input:
        board.append(list(line))

    #Find blank rows
    blank_rows = []
    for i,row in enumerate(board):
        if row.count(".") == len(row):
            blank_rows.append(i)


    #find blank columns
    blank_cols = []
    dot_count = 0

    for i in range(len(board[0])):
        dot_count = 0

        for j in range(len(board)):
            if board[j][i] == ".":
                dot_count += 1
            else:
                break

        if dot_count == len(board):
            blank_cols.append(i)

    #big_board = add_repeats(board, blank_cols, blank_rows)

    galaxies = galaxy_parse(raw_input)

    galaxies_adjusted = galaxy_adjuster(galaxies, blank_rows, blank_cols)

    list_of_distances = dist_getter(galaxies_adjusted)

    total = 0
    for pairs in list_of_distances:
        for dist in pairs:
            total+=dist

    print(total)
    print("done")


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))