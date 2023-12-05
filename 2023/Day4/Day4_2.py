try:
    import logging
    import os
    import re
    import timeit
except:
    print("Imports failed")

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

class Card:
    def __init__(self, raw_data, original):
        self.card_number = 0
        self.winning = set()
        self.numbers = set()
        self.original = original

        self.parse_data(raw_data)
        self.winning_numbers = self.check_winners()
        self.win_len = len(self.winning_numbers)

        self.score = self.calculate_score()


    def parse_data(self, raw_data):
        self.card_number = int(re.search(r"(?:[0-9]+)",raw_data).group())
        win_and_numbers  = raw_data.split(":")[1]
        winning = win_and_numbers.split("|")[0].strip()
        numbers = win_and_numbers.split("|")[1].strip()

        for num in re.finditer(r"(?:[0-9]+)", winning):
            self.winning.add(num.group())

        for num in re.finditer(r"(?:[0-9]+)",numbers):    
            self.numbers.add(num.group())


    def check_winners(self):

        return list(self.winning.intersection(self.numbers))

    def calculate_score(self):
        length = len(self.winning_numbers)
        score = 1

        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            for i in range(length-1):
                score *= 2
            return score

    def __repr__(self):
        str = "Card {}. winners:{}, score {}, Original:{}".format(self.card_number, self.winning_numbers, self.score, self.original)
        return(str)

    def __str__(self):
        return(self.__repr__())


def parse_cards(raw_input):
    cards = []
    for line in raw_input:
        cards.append(Card(line, original = True))

    return cards

def main():
    raw_input = get_input()
    original_cards = parse_cards(raw_input) #basically parsed input

    extended_cards = original_cards.copy()
    #based on the original cards' winners. add copies of cards to list
    for val, card in enumerate(extended_cards):
        for i in range(card.win_len):
            card_buf = original_cards[card.card_number+i]
            card_buf.original = False
            extended_cards.append(card_buf)

    print(len(extended_cards))
    
    print("done")


if __name__ == "__main__":
    try:
        total_time = timeit.timeit('main', number=1, globals=globals())
        #main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    print('Average time: {} usec'.format((total_time/1)*1e6))