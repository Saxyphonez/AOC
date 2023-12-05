try:
    import logging
    import os

except:
    print("Imports failed")

TEST = not True

RED_LIM = 12
GREEN_LIM = 13
BLUE_LIM = 14

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"


class Game:

    def __init__(self, ID, game_text):
        self.gameID = ID
        self.game_is_possible = True
        self.game_text = game_text.strip() #each of the draws, separated by semicolons
        self.num_draws = game_text.count(";") + 1

        #dict: {<drawID>: [R,G,B]}
        self.draws = {}
        self.parse_game(self.game_text)


    def parse_game(self, game_text):
        draws_separated = game_text.split(";")

        for i in range(self.num_draws):
            current_draw = draws_separated[i]
            #print(current_draw)
            rgb_buf, set_is_possible = self.get_RGB(current_draw)

            if set_is_possible == False:
                self.game_is_possible = False

            self.draws[i] = rgb_buf
            #dict: {<drawID>: [R,G,B]}


    def get_RGB(self, text):
        rgb = [0,0,0]
        set_is_possible = True

        text_split = text.split(",")
        text_split = [x.strip() for x in text_split]

        for ball in text_split:
            buf = ball.split(" ")
            number = int(buf[0])
            colour = buf[1]

            match(colour):
                case "red":
                    rgb[0] = number
                    if number > RED_LIM:
                        set_is_possible = False
                case "green":
                    rgb[1] = number
                    if number > GREEN_LIM:
                        set_is_possible = False
                case "blue":
                    rgb[2] = number
                    if number > BLUE_LIM:
                        set_is_possible = False

        return rgb, set_is_possible

    def is_possible(self):
        return self.game_is_possible
    
    def __repr__(self):
        str = "ID:{}, Sets:{}, Possible:{}".format(self.gameID, 
                                                    self.num_draws, self.game_is_possible)
        return(str)
    
    def __str__(self):
        str = "ID:{}, Sets:{}, Possible:{}".format(self.gameID, 
                                                    self.num_draws, self.game_is_possible)
        return str


def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)
    with open(input_filepath,'r') as f:
        input = f.readlines()

    input = [line.strip() for line in input]
    return input

def main():
    raw_games = get_input()
    games = []

    for i, game in enumerate(raw_games):
        games.append(Game(ID = i+1, game_text = game.split(":")[1]))
        
    total = 0
    for game in games:
        if game.is_possible():
            print("Game{} is possible".format(game.gameID))
            total += game.gameID

    print(total)
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")