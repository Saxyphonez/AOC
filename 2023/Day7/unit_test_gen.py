import itertools
import os
import random

NUM_CARDS = 5
CARDS = []
FACE_CARDS = "TJQKA"
for i in range (2,10):
    CARDS.append(str(i))

CARDS.extend(list(FACE_CARDS))

big_list = itertools.product(CARDS, repeat = NUM_CARDS)

lst = []
for subset in big_list:
    lst.append(''.join(subset))

input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "unit_test.txt")
#print(input_filepath)
random.shuffle(lst)


with open(input_filepath,'w') as f:
    for item in lst:
    # write each item on a new line
        f.write("%s 1\n" % item)
print('Done')