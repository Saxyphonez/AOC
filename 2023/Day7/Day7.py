try:
    import logging
    import os
    import timeit
    from enum import Enum

except:
    print("Imports failed")

TEST = True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

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
        self.type = self.get_HandType(self.hand)


    def get_HandType(self, hand_txt):
        print("start")
        #(A{5})|(K{5})|(Q{5})|(T{5})|(J{5})
        for i in range (5,1,-1):
            regex_txt = "(A{s})|(K{s})|(Q{s})|(T{s})|(J{s})".format(s=i)
            print(regex_txt)

        return True


    def __repr__(self):
        str = "Hand {} Bid {}".format(self.raw_hand, self.bid_int)
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