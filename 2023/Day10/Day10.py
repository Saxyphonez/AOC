try:
    import logging
    import os
    import timeit
    import re
    from enum import Enum

except:
    print("Imports failed")

TEST = not True

if TEST:
    #input_filename = "test_input.txt"
    input_filename = "test_input2.txt"

else:
    input_filename = "input.txt"

class Direction(Enum):
    NORTH_SOUTH = 0,
    WEST_EAST = 1,

    NORTH_EAST = 2,
    NORTH_WEST = 3,

    SOUTH_WEST = 4,
    SOUTH_EAST = 5,

    GND = 6
    START = 7


class Pipe:
    def __init__(self, raw_pipe, row, col):
        self.name = "TEMP"
        self.col = col
        self.row = row

        self.type = None
        self.coord = (self.row, self.col)
        self.connections = [(self.row,self.col), (self.row,self.col)]

        self.visited = False

        self.parse(raw_pipe)

    def parse(self, raw_pipe):
        self.name = raw_pipe
        match raw_pipe:
            case "|":
                self.type = Direction.NORTH_SOUTH
                self.connections = [(self.row-1,self.col), (self.row+1,self.col)]

            case "-":
                self.type = Direction.WEST_EAST
                self.connections = [(self.row,self.col-1), (self.row,self.col+1)]

            case "L":
                self.type = Direction.NORTH_EAST
                self.connections = [(self.row-1,self.col), (self.row,self.col+1)]

            case "J":
                self.type = Direction.NORTH_WEST
                self.connections = [(self.row-1,self.col), (self.row,self.col-1)]

            case "7":
                self.type = Direction.SOUTH_WEST
                self.connections = [(self.row+1,self.col), (self.row,self.col-1)]

            case "F":
                self.type = Direction.SOUTH_EAST
                self.connections = [(self.row+1,self.col), (self.row,self.col+1)]

            case ".":
                self.type = Direction.GND

            case "S":
                self.type = Direction.START

            case _:
                print("Error parsing pipe")


    def __repr__(self):
        #str = "Pipe {} col:{}, row:{}".format(self.name, self.col, self.row)
        str = "{} r{},c{}".format(self.name, self.row, self.col)
        return(str)
    
    def __str__(self):

        return "Pipe {} r:{}, c:{}".format(self.name, self.row, self.col)
    
class Board:
    def __init__(self, raw_data):
        self.name = "Board"
        self.start_point = None
        self.grid = self.create_grid(raw_data)
        


    def create_grid(self, raw_data):
        board = []

        for i, line in enumerate(raw_data):
            line_lst = list(line)
            row_span = len(line_lst)

            line_buf = []

            for j, pipe in enumerate(line_lst):
                pipe_temp = Pipe(pipe, row = i, col = j)
                line_buf.append(pipe_temp)

                if pipe_temp.type == Direction.START:
                    self.start_point = pipe_temp
            
            board.append(line_buf)
        
        return board

    def get_start_point(self):

        return self.start_point

    def __repr__(self):
        str = "{}".format(self.grid)
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

def find_connections(point, grid, start = True):
    conns = []

    point_coord = (point.row, point.col)

    if not start:
        if (point_coord in grid[point.row][point.col-1].connections):
            if (grid[point.row][point.col-1].coord in point.connections):
                conns.append(grid[point.row][point.col-1])

        if point_coord in grid[point.row][point.col+1].connections:
            if (grid[point.row][point.col+1].coord in point.connections):
                conns.append(grid[point.row][point.col+1])

        if point_coord in grid[point.row-1][point.col].connections:
            if (grid[point.row-1][point.col].coord in point.connections):
                conns.append(grid[point.row-1][point.col])

        if point_coord in grid[point.row+1][point.col].connections:
            if (grid[point.row+1][point.col].coord in point.connections):
                conns.append(grid[point.row+1][point.col])

    else:
        if (point_coord in grid[point.row][point.col-1].connections):        
            conns.append(grid[point.row][point.col-1])

        if point_coord in grid[point.row][point.col+1].connections:
            conns.append(grid[point.row][point.col+1])

        if point_coord in grid[point.row-1][point.col].connections:
            conns.append(grid[point.row-1][point.col])

        if point_coord in grid[point.row+1][point.col].connections:
            conns.append(grid[point.row+1][point.col])

    #remove previously visited
    conns_clean = []
    for i, conn in enumerate(conns):
        if conn.visited == True:
            continue
        else:
            conns_clean.append(conn)

    return conns_clean


def main():
    raw_input = get_input()

    board = Board(raw_input)

    start = board.get_start_point()
    
    start_row = start.row
    start_col = start.col
    start_coord = (start_row, start_col)

    grid = board.grid

    #Find pipes connected to the start:
    start_conns = find_connections(start, grid, True)
    

    #Build a graph/map:
    current_points = start_conns.copy()
    
    looped = False
    graph = {}
    


    while not looped:
        next_points = []

        if len(current_points) > 0:
            for point in current_points:
                point.visited = True
                next_points.extend(find_connections(point, grid, False))
                graph[point] = find_connections(point, grid, False)

            for point in graph.keys():
                if point.type == Direction.START:
                    print("back to start")
                    looped = True
                    break
                else:
                    continue

            current_points = next_points.copy()
        else:
            looped = True
        
    graph[start] = start_conns

    for point in graph.keys():
        if len(graph[point]) ==  0:
            end = point

    #traverse back from end to start?
    reached  = False
    step = 1
    current = graph[start][0]

    while not reached:
        next = graph[current][0]

        if next == end:
            reached = True
        else:
            current = next
            step += 1

    print(step+1)
    print("done")


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))