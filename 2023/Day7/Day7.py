try:
    import logging
    import os
    import timeit
    from enum import Enum
    import re
    #from sort import *

except:
    print("Imports failed")

TEST = not True
UNIT_TEST = False

if TEST:
    input_filename = "test_input.txt"
    #input_filename = "unit_test.txt"
    output_filename = "sorted.txt"
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

        self.hand_txt = list(self.raw_hand)
        self.hand_ints = self.gen_hand_ints(self.hand_txt)
        self.type = HandType.NONE

        self.get_HandType(self.hand_txt)

    def gen_hand_ints(self, hand_txt):
        hand_int = []
        for card in hand_txt:
            hand_int.append(CARDS.index(card))

        return hand_int

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

def quick_sort(hands_lst, func_i = 0):
    
    if len(hands_lst) <= 1:
        return hands_lst

    elif len(hands_lst) == 2:
        left = []
        right = []
        other_hand = hands_lst[0]
        pivot = hands_lst[1]

        for i in range(0,len(pivot.hand_ints)):
            #print("{} vs {}".format(other_hand.hand_ints[i], pivot.hand_ints[i]))

            if other_hand.hand_ints[i] > pivot.hand_ints[i]:
                right.append(other_hand)
                left.append(pivot)
                break

            elif other_hand.hand_ints[i] < pivot.hand_ints[i]:
                left.append(other_hand)
                right.append(pivot)
                break

            elif other_hand.hand_ints[i] == pivot.hand_ints[i]:
                continue

            else:
                print("Identical")

        return left + right
            

    else:
        left = []
        middle = []
        right = []
        pivot_hand = hands_lst[len(hands_lst)//2]
        pivot = pivot_hand.hand_ints

        for hand in hands_lst:
            #print(hand)
            for i in range(0,len(pivot)):
                #("{} vs {}".format(hand.hand_ints[i], pivot[i]))
                if hand.hand_ints[i] > pivot[i]:
                    right.append(hand)
                    break

                elif hand.hand_ints[i] < pivot[i]:
                    left.append(hand)
                    break

                elif hand.hand_ints[i] == pivot[i]:
                    continue


        return quick_sort(left) + [pivot_hand] + quick_sort(right)


def main():
    #parse input
    raw_input = get_input()

    #create hands
    hands = []
    hands_five = []
    hands_four = []
    hands_three = []
    hands_full = []
    hands_two = []
    hands_one = []
    hands_high = []

    

    for line in raw_input:
        hand_buf = Hand(line)
        #hands.append(hand_buf)

        match hand_buf.type:
            case HandType.FIVE_KIND:
                hands_five.append(hand_buf)

            case HandType.FOUR_KIND:
                hands_four.append(hand_buf)

            case HandType.THREE_KIND:
                hands_three.append(hand_buf)

            case HandType.FULL_HOUSE:
                hands_full.append(hand_buf)

            case HandType.TWO_PAIR:
                hands_two.append(hand_buf)

            case HandType.ONE_PAIR:
                hands_one.append(hand_buf)

            case HandType.HIGH_CARD:
                hands_high.append(hand_buf)

    #perform the comparisons
    list_of_list = [hands_five, hands_four, hands_full, 
                    hands_three, hands_two, hands_one, 
                    hands_high]
    list_of_list.reverse()

    sorted = []
    for group in list_of_list:
        if len(group) == 0:
            continue
        else:
            sorted.extend(quick_sort(group, 0))

    if UNIT_TEST:
        output_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), output_filename)
        with open(output_filepath,'w') as f:
            for item in sorted:
            # write each item on a new line
                f.write("%s\n" % item)
        return

    #print(sorted)
    total = 0

    for i, hand in enumerate(sorted):
        #print("Bid {} * {}".format(hand.bid_int, i+1))
        total += hand.bid_int * (i+1)

    print(total)
    print("done")


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))