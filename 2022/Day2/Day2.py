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

def score_for_opt(throw):
    match throw:
        case 'X':
            return ROCK
        case 'Y':
            return PAPER
        case 'Z':
            return SCIS

def do_turn(throws):
    score = 0
    opponent = throws[0]
    player = throws[1]

    #A Rock X = 1 pt
    #B Paper Y = 2 pt
    #C Scissors Z = 3 pt
    # win = 6pt
    # draw = 3 pt
    # lose = 0 pt

    if (opponent == 'A' and player == 'X') or (opponent == 'B' and player == 'Y') or (opponent == 'C' and player == 'Z'):
        #draw
        score = DRAW
        match player:
            case 'X':
                score+=1
            case 'Y':
                score+=2
            case 'Z':
                score+=3
        return score
    
    if opponent == 'A':
        if player == 'Y':
            score = WIN + PAPER
        else:
            score = score_for_opt(player)

    elif opponent == 'B':
        if player == 'Z':
            score = WIN + SCIS
        else:
            score = score_for_opt(player)

    elif opponent == 'C':
        if player == 'X':
            score = WIN + ROCK
        else:
            score = score_for_opt(player)

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