try:
    import logging
    import os
    import sys

    # import re
    from enum import Enum

except ModuleNotFoundError or ImportError as e:
    print("Imports failed")
    print(e)

TEST = not True
GUARD_CHAR = "^"
EMPTY_SPACE = "."

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

class Direction(Enum): # Direction guard is facing
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

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



    board, guard_row_start, guard_column_start = generate_board(input)
    length = len(board)
    width = len(board[0])

    map = generate_obstacle_graph(board, length, width)

    # print("=== DEFAULT ===")
    # for key, value in map.items():
    #     print("{}: {}".format(key, value))

    # print("\r\n")

    guard_direction_start = Direction.UP


    
    visited_spaces = part_one()
    total = len(visited_spaces)
    possible_obstacle_locations = []

    for i, coord in enumerate(visited_spaces):
        
        

        possible_row = coord[0]
        possible_column = coord[1]

        if board[possible_row][possible_column] != "#":
            board[possible_row][possible_column] = "#"
        else:
            continue


        map = generate_obstacle_graph(board, length, width)

        guard_slow = Guard(id=0, row=guard_row_start, column=guard_column_start, direction=guard_direction_start, fast=False, map_in=map)
        guard_fast = Guard(id=1, row=guard_row_start, column=guard_column_start, direction=guard_direction_start, fast=True, map_in=map)
        
        current_obs_coord = ()

        for r in range (guard_slow.row-1, 0-1, -1):
            check_coord = (r, guard_slow.column)
            if(check_coord in map):
                current_obs_coord = check_coord
                #print("First obstacle hit is at {}".format(check_coord))
                break

            else:
                continue
        
        guard_slow.set_coord(get_next_guard_position(current_obs_coord, guard_slow.direction))
        guard_fast.set_coord(get_next_guard_position(current_obs_coord, guard_fast.direction))
        guard_slow.set_current_obstacle(current_obs_coord)
        guard_fast.set_current_obstacle(current_obs_coord)

        guard_slow.next_position()
        guard_fast.next_position()
        guard_fast.next_position()

        in_loop = False

        while(not in_loop):
            ret_slow = guard_slow.next_position()

            ret_fast_first =guard_fast.next_position()
            ret_fast_second = guard_fast.next_position()

            if(ret_fast_first and ret_fast_second and ret_slow):
                slow_coords = guard_slow.get_coord()
                fast_coords = guard_fast.get_coord()

                if(slow_coords == fast_coords):
                    possible_obstacle_locations.append((possible_row, possible_column))

                    print("({}/{})Loop detected. Possible obstacle placement at {}. Len now:{}"
                        .format(i, total, (possible_row, possible_column), len(possible_obstacle_locations)))
                    
                    in_loop = True
            else:
                break


        
        #at the end make it back to a dot
        board[possible_row][possible_column] = "."

    print("Answer is {}".format(len(possible_obstacle_locations)))
    print("Done!")


def part_one():
    input = get_input()



    board, guard_row_start, guard_column_start = generate_board(input)
    length = len(board)
    width = len(board[0])



    map = generate_obstacle_graph(board, length, width)

    guard_row, guard_column = 0, 0
    guard_direction_start = Direction.UP
    visited_points = [] # [row,col]

    #run the simulation
    #from guards starting point
    guard_direction = Direction.UP
    guard_row = guard_row_start
    guard_column = guard_column_start

    current_obs_coord = ()

    # find first obstacle
    # heading upwards so check row_1 to row==0 and column = start column
    for r in range (guard_row-1, 0-1, -1):
        check_coord = (r, guard_column)
        if(check_coord in map):
            current_obs_coord = check_coord
            #print("First obstacle hit is at {}".format(check_coord))
            break

        else:
            continue

    points_between = coords_between((guard_row, guard_column), (current_obs_coord[0], current_obs_coord[1]), guard_direction, length, width)

    for point in points_between:
        visited_points.append(point)

    guard_row, guard_column = get_next_guard_position(current_obs_coord, guard_direction)
    #print("next posn {}".format((guard_row, guard_column)))
    guard_direction = next_direction(guard_direction) # change direction after hitting first obstacle!
    
    

    #now that we have the first obstacle. We can traverse the map
    #based on current direction, check what the next neighbour is in the dirn 90degrees right
    guard_off_board = False


    while(not guard_off_board):
        points_between = []

        next_obstacle = get_next_obstacle(map, current_obs_coord, guard_direction)

        if(next_obstacle is not None):
            next_row, next_column = get_next_guard_position(next_obstacle, guard_direction)



        if(next_obstacle is None):
            #print("Gone off board from travelling {}-wards from {}".format(guard_direction.name, (guard_row, guard_column)))
            points_between = coords_between((guard_row, guard_column), next_obstacle, guard_direction, length, width)

            for point in points_between:
                if point in visited_points:
                    continue
                else:
                    visited_points.append(point)

            guard_off_board = True
        
        else:

            points_between = coords_between((guard_row, guard_column), (next_obstacle[0], next_obstacle[1]), guard_direction, length, width)

            for point in points_between:
                if point in visited_points:
                    continue
                else:
                    visited_points.append(point)

            current_obs_coord = next_obstacle
            #print("next posn {}".format((next_row, next_column)))
            guard_row = next_row
            guard_column = next_column
            guard_direction = next_direction(guard_direction)

    return visited_points



def coords_between_offmap(length, width, start, direction):
    coord_list = []
    start_row = start[0]
    start_column = start[1]

    match(direction):
        case Direction.UP:
            for i in range(start_row, 0, -1):
                coord_list.append((i,start_column))


        case Direction.RIGHT:
            for i in range(start_column, width):
                coord_list.append((start_row,i))          

        case Direction.DOWN:
            for i in range(start_row, length):
                coord_list.append((i,start_column))

        case Direction.LEFT:
            for i in range(start_column, 0, -1):
                coord_list.append((start_row,i))          
        case _:
            print("Offmap Error!")

    return coord_list




def coords_between(start, end, direction, length, width):
    coord_list = []
    
    start_row = start[0]
    start_column = start[1]

    if(end is not None):
        end_row = end[0]
        end_column = end[1]

        match(direction):
            case Direction.UP:
                for i in range(start_row, end_row, -1):
                    coord_list.append((i,start_column))


            case Direction.RIGHT:
                for i in range(start_column, end_column):
                    coord_list.append((start_row,i))          

            case Direction.DOWN:
                for i in range(start_row, end_row):
                    coord_list.append((i,start_column))

            case Direction.LEFT:
                for i in range(start_column, end_column, -1):
                    coord_list.append((start_row,i))          
            case _:
                print("Next direction Error!")

    else:
        match(direction):
            case Direction.UP:
                for i in range(start_row, 0, -1):
                    coord_list.append((i,start_column))


            case Direction.RIGHT:
                for i in range(start_column, width):
                    coord_list.append((start_row,i))          

            case Direction.DOWN:
                for i in range(start_row, length):
                    coord_list.append((i,start_column))

            case Direction.LEFT:
                for i in range(start_column, 0, -1):
                    coord_list.append((start_row,i))          
            case _:
                print("Offmap Error!")        

    return coord_list


def get_next_obstacle(map, start_coord, direction):
    neighbours = map[start_coord]

    next = neighbours[direction.value]
    return next


#Gets the guard's coordinates based on the direction they were travelling
#when they hit the obstacle and the obstacle's coordinates
def get_next_guard_position(obstacle_coord, guard_direction):

    guard_row = 0
    guard_column = 0

    obstacle_row = obstacle_coord[0]
    obstacle_column = obstacle_coord[1]

    
    match(guard_direction):
        case Direction.UP:
            guard_row = obstacle_row + 1
            guard_column = obstacle_column

        case Direction.RIGHT:
            guard_row = obstacle_row 
            guard_column = obstacle_column - 1

        case Direction.DOWN:
            guard_row = obstacle_row - 1
            guard_column = obstacle_column

        case Direction.LEFT:
            guard_row = obstacle_row 
            guard_column = obstacle_column + 1

        case _:
            print("Guard positioning - Direction Error!")


    return guard_row, guard_column


def generate_obstacle_graph(board, length, width):
    map = {}

    obstacle_coord_list = []

    #get a list of all the obstacles
    for r,row in enumerate(board):
        for c, col in enumerate(row):
            if(col == "#"):
                obstacle_coord_list.append((r, c))

            else:
                continue
            
    #for each obstacle, find its neighbour in a possible direction
    for i, obstacle_coord in enumerate(obstacle_coord_list):
        obs_row = obstacle_coord[0]
        obs_column = obstacle_coord[1]

        possible_directions = [False]*4
        neighbours = [None] * 4 


        #get possibilites of positions including edge cases:
        up = True if obs_row-1>0 else False
        right = True if obs_column+1<=width-1 else False
        down = True if obs_row+1<=length-1 else False
        left = True if obs_column-1>0 else False
        
        possible_directions = [up, right, down, left]


        for i, direction in enumerate(possible_directions):
            #get the coords of the neighbour
            #accounting for the fact the guard stops 1 shy of the actual object
            # i here corresponds to the Direction Enum
            if(not direction):
                # if a direction is not possible, put none 
                neighbours[i] = None
                continue

            #This only works for turning right 90degrees upon reaching an obstacle
            match (i):
                case 0: #UP
                    #check from current row-1 down to row==0 and col+1
                    for check_row in range(obs_row-1, -1, -1):
                        check_coord = (check_row, obs_column+1)
                        if(check_coord in obstacle_coord_list):
                            neighbours[i] = check_coord
                            break

                        else:
                            continue

                    
                case 1: #RIGHT
                    #check current col+1 up to col==width and row+1
                    for check_col in range(obs_column+1, width+1):
                        check_coord = (obs_row+1, check_col)
                        if(check_coord in obstacle_coord_list):
                            neighbours[i] = check_coord
                            break
                        
                        else:
                            continue

                case 2: #DOWN
                    #check current current row+1 up to row==length and col-1
                    for check_row in range(obs_row+1, length+1):
                        check_coord = (check_row, obs_column-1)
                        if(check_coord in obstacle_coord_list):
                            neighbours[i] = check_coord
                            break
                        
                        else:
                            continue

                case 3:#LEFT
                    #check current col-1 up to col==0 and row-1
                    for check_col in range(obs_column-1, 0-1, -1):
                        check_coord = (obs_row-1, check_col)
                        if(check_coord in obstacle_coord_list):
                            neighbours[i] = check_coord
                            break
                        
                        else:
                            continue



                case _:
                    print("Error in checking neighbours in a direction")
        
        #generate obstable node
        #{(tuple of obstacle coord): [list of neighour obstacle coord tuples]}
        map[(obs_row, obs_column)] = neighbours
        #add that to a list or soemthing


    return map


def next_direction(current_direction):
    next = None

    match(current_direction):
        case Direction.UP:
            next = Direction.RIGHT

        case Direction.RIGHT:
            next = Direction.DOWN

        case Direction.DOWN:
            next = Direction.LEFT

        case Direction.LEFT:
            next = Direction.UP            
        case _:
            print("Next direction Error!")

    if (next is not None):
        return next
    
    else:
        print("Next direction was None!")
        return next


def generate_board(input):

    board = [list(x) for x in input]

    guard_row = 0
    guard_col = 0

    for i, row in enumerate(board):
        board[i] = list(row)
        if(GUARD_CHAR in row):
            guard_row = i
            guard_col = row.index(GUARD_CHAR)
            board[i][guard_col] = EMPTY_SPACE


    return board, guard_row, guard_col


class Guard():

    

    def __init__(self, id, row, column, direction, fast, map_in):
        self.id = id
        self.row = row
        self.column = column
        self.direction = direction
        self.fast = fast
        self.map = map_in
        self.current_obstacle = None
        self.next_obstacle = None

        self.coord = (self.row, self.column)
        pass

    
    def set_coord(self, coord):
        self.row = coord[0]
        self.column = coord[1]
        self.coord = (self.row, self.column)

    def get_coord(self):
        return self.coord

    def set_direction(self, direction):
        self.direction = direction
    
    def next_position(self):
        self.next_direction()
        self.next_obstacle = get_next_obstacle(self.map, self.current_obstacle, self.direction)

        if (self.next_obstacle is not None):
            self.set_coord(get_next_guard_position(self.next_obstacle, self.direction))
            self.current_obstacle = self.next_obstacle
            return 1
        else:
            return 0
        
        

    def next_direction(self):
        self.direction = next_direction(self.direction)

    def set_current_obstacle(self, obstacle_coord):
        self.current_obstacle = obstacle_coord


    def __repr__(self):
        return self.__str__()

    def __str__(self):

        return "Guard[{}] at ({}) facing ".format(self.id, self.coord, self.direction.name)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")
