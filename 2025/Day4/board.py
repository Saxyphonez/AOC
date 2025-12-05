try:
    from random import randint
    import random
    import time

except ModuleNotFoundError or ImportError as e:
    print("{} Import error:".format(__name__))
    print(e)

# [DEAD, ALIVE]
POSSIBLE_CHARSETS = [
    [".", "@"], #[SPACE,ROLL]
    [" ", "#"],
    [".", "#"],
    [" ", "@"],
    [".", "@"],
    [" ", "1"],
    ["0", "1"],
    [".", "1"],
    ["0", "  "],#Purposefully reversed
]

class Board():

    cells = []
    rows = None
    cols = None
    seed = None
    threshold = None
    selected_charset = POSSIBLE_CHARSETS[0]

    char_space = None
    char_roll = None

    def __init__(self, rows, cols, seed = None, threshold = 6) -> None:
        
        self.rows = rows
        self.cols = cols
        self.threshold = threshold

        self.char_space = self.selected_charset[0]
        self.char_roll = self.selected_charset[1]

        if(seed is None):
            self.seed = time.time()
        else:
            self.seed = seed
        

        for i in range(self.rows):
            temp = [0]*self.cols
            self.cells.append(temp)
        

        random.seed(self.seed)
        #self.random_state()


    def random_state(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.cells[r][c] = 0 if randint(1,10) < self.threshold else 1


    def get_cell(self, row, col):

        return self.cells[row][col]



    def get_neighbours(self, row, col):
        neighbours = []

        row_lim_lower = row-1 if ((row-1) >= 0) else row
        row_lim_upper = row+1 if ((row+1) <= self.rows-1) else row

        col_lim_lower = col-1 if ((col-1) >= 0) else col
        col_lim_upper = col+1 if ((col+1) <= self.cols-1) else col


        for r in range(row_lim_lower, row_lim_upper+1):
            for c in range(col_lim_lower, col_lim_upper+1):
                if ((r == row) and (c==col)):
                    continue

                neighbours.append(self.get_cell(r,c))

        return neighbours



    # def next_state(self):


    #     pass

    def set_charset(self, idx):
        if idx >= 0 and idx<len(POSSIBLE_CHARSETS):
            self.selected_charset = POSSIBLE_CHARSETS[idx]
        else:
            self.selected_charset = POSSIBLE_CHARSETS[0]

        self.char_space = self.selected_charset[0]
        self.char_roll = self.selected_charset[1]



    def render(self):
        rows = self.rows
        cols = self.cols

        bars = ["-"]*(cols+4)
        print(''.join(bars))

        for r in range(rows):
            for c in range(cols):
                if(c == 0):
                    print("| ", end="")
                cell = self.cells[r][c]

                if(cell == 0):
                    print(self.char_space, end="")
                else:
                    print(self.char_roll, end="")

                if(c == cols-1):
                    print(" |", end="")

                if c+1 % cols == 0:
                    print("")

            print("")

        print(''.join(bars))


    def __repr__(self) -> str:
        
        return self.__repr__()

    def __str__(self) -> str:

        return "r:{} c:{} -> {}".format(self.rows, self.cols, self.cells)