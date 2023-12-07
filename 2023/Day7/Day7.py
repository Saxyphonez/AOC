try:
    import logging
    import os
    import timeit
    from enum import Enum
    import re

except:
    print("Imports failed")

TEST = True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

CARDS = []
FACE_CARDS = "TJQKA"
for i in range (2,10):
    CARDS.append(str(i))

CARDS.extend(list(FACE_CARDS))



class HandType(Enum):
    NONE = 7 #just in case

    FIVE_KIND  = 6
    FOUR_KIND  = 5
    THREE_KIND  = 4
    FULL_HOUSE  = 3
    TWO_PAIR  = 2
    ONE_PAIR  = 1
    HIGH_CARD  = 0


class Hand():
    def __init__(self, raw_data):
        self.raw_hand = raw_data.split(" ")[0].strip()
       

        self.bid = raw_data.split(" ")[1].strip()
        self.bid_int= int(self.bid)

        self.hand = list(self.raw_hand)
        self.get_HandType(self.hand)


    def get_HandType(self, hand_txt):
        output = {}
        for x in CARDS:
            cnt = list(hand_txt).count(x)
            if cnt > 0:
                output[x] = cnt

        max_cnt = output[max(output, key = output.get)]

        if max_cnt == 5:
            self.type = HandType.FIVE_KIND

        elif max_cnt == 4:
            self.type = HandType.FOUR_KIND

        elif max_cnt == 3:
            print(min(output, key = output.get))
            if output[min(output, key = output.get)] == 1:
                self.type = HandType.THREE_KIND
            else:
                self.type = HandType.FULL_HOUSE

        elif max_cnt == 2:
            occurences = list(output.values())

            if occurences.count(2) == 2:
                self.type = HandType.TWO_PAIR
            else:
                self.type = HandType.ONE_PAIR

        else:
            self.type = HandType.HIGH_CARD

                

    def __repr__(self):
        str = "Hand {} Bid {} Type {}".format(self.raw_hand, self.bid_int, self.type)
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

def main():
    #parse input
    raw_input = get_input()

    #create hands
    hands = []
    for line in raw_input:
        hands.append(Hand(line))

    #perform the comparisons

    print("done")


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))