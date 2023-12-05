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
    def __init__(self,map_details):
        
        #fill these text feels in for repr str to make debug easier
        self.source_txt,\
            self.dest_text = self.get_source_dest(map_details)

        #x y z
        #dest start, source start, range
        #sources = [range(y,y+z-1)] dests = [range(x,x+z-1)]. query sets?
        #else 1-to-1

        self.map_dict = self.create_map(map_details) #key=source: val=destination

    def get_source_dest(self,details):
        hyphenated = details[0]
        hyphenated = hyphenated.split(" ")
        source = hyphenated[0].split("-")[0]
        dest = hyphenated[0].split("-")[2]

        return source, dest


    def create_map(self, details):
        map_dict = {}
        ranges = details[1:-1]
        max_source = 0

        for details in ranges:
            range_details = details.strip().split(" ")
            source_start = int(range_details[1])
            destination_start = int(range_details[0])
            range_size = int(range_details[2])

            source_range = [*range(source_start, source_start+range_size)]
            destination_range = [*range(destination_start, destination_start+range_size)]

            for i, source in enumerate(source_range):
                map_dict[source] = destination_range[i]
                if source > max_source:
                    max_source = source

        map_dict_sorted = dict(sorted(map_dict.items()))


        for i in range(0, max_source):
            if i not in map_dict_sorted.keys():
                map_dict_sorted[i] = i

        map_dict_full = dict(sorted(map_dict_sorted.items()))

        return map_dict_full


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

    #get index of all newline char
    line_break_index = [i for i, line in enumerate(input) if line=="\n"]
    print([i+1 for i in line_break_index])

    output = []
    output.append([input[0]])
    for i in range(0, len(line_break_index)):
        if i == len(line_break_index)-1:
            output.append(input[line_break_index[i]+1:-1])
        else:
            output.append(input[line_break_index[i]+1:line_break_index[i+1]])

    return output

def main():
    raw_input = get_input()
    seeds_input = raw_input[0]
    maps_input = raw_input[1:]

    #parse input and create maps
    map_list = []
    seed_list = []
    for i, map in enumerate(maps_input):
        map_list.append(Map(map))

    #parse input and create seeds
    #for i, seed in enumerate(seeds_input):
        #seed_list.append(Seed(seed, map_list)) #TODO fix

    print("done")


if __name__ == "__main__":
    try:
        #ßtotal_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))