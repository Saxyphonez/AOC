try:
    import logging
    import os
    import timeit

except:
    print("Imports failed")

TEST = True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

class Map:
    def __init__(self,name, map_details):
        
        #fill these text feels in for repr str to make debug easier
        self.name = name
        self.source_txt = ""
        self.dest_text = ""

        #x y z
        #dest start, source start, range
        #sources = [range(y,y+z-1)] dests = [range(x,x+z-1)]. query sets?
        #else 1-to-1

        self.map_dict = create_dict(map_details) #key=source: val=destination

    def create_map(self, details):
        map_dict = {}


        return map_dict

    def follow(self, source):
        return self.map_dict[source]

    def __repr__(self):
        str = "Map {} to {} ".format(self.source_txt, self.dest_text)
        return(str)

    def __str__(self):
        return(self.__repr__())

class Seed:
    def __init__(self,number, map_list):
        
        self.details = [None]*8

        self.seed = number
        # self.soil = None
        # self.fert = None
        # self.water = None

        # self.light = None
        # self.temp = None
        # self.humid = None
        # self.loc = None

        self.follow_map(map_list)
        self.loc = self.details[-1]
            

    def follow_map(self, map_list):
        for i in range(0,8):
            if i==0:
                self.details[i] = self.seed
            else:
                self.details[i] = map_list[i].follow(source = self.details[i-1])


    def __repr__(self):
        str = "Seed{}".format(self.number)
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
    raw_input = get_input

    #parse input and create maps

    #parse input and create seeds

    print("done")


if __name__ == "__main__":
    try:
        total_time = timeit.timeit('main', number=1, globals=globals())
        #main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    print('Average time: {} usec'.format((total_time/1)*1e6))