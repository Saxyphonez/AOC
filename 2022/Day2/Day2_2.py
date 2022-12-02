try:
    import logging
    import os

except:
    print("Imports failed")

TEST = not True


DRAW = 3
WIN = 6
LOSE = 0

ROCK = 1
PAPER = 2
SCIS = 3

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    buffer = []

    for i, val in enumerate(input):
        buffer.append(val.strip().split(" "))


    return buffer

def move_for_outcome(opponent, outcome):
    if outcome == WIN:
        match opponent:
            case 'A':
                return PAPER
            case 'B':
                return SCIS
            case 'C':
                return ROCK

    elif outcome == DRAW:
        match opponent:
            case 'A':
                return ROCK
            case 'B':
                return PAPER
            case 'C':
                return SCIS 

    elif outcome == LOSE:
        match opponent:
            case 'A':
                return SCIS
            case 'B':
                return ROCK
            case 'C':
                return PAPER



def do_turn(throws):
    score = 0
    opponent = throws[0]
    player = throws[1]

    #A Rock = 1 pt
    #B Paper = 2 pt
    #C Scissors = 3 pt
    # Z win = 6pt
    # Y draw = 3 pt
    # Xlose = 0 pt
    match player:
        case 'Z':
            score = WIN + move_for_outcome(opponent, WIN)
        
        case 'Y':
            score = DRAW + move_for_outcome(opponent, DRAW)
        
        case 'X':
            score = LOSE + move_for_outcome(opponent, LOSE)

    
    return score

def main():

    input = get_input()
    score = 0

    for i, val in enumerate(input):
        score += do_turn(val)
    print(score)

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")