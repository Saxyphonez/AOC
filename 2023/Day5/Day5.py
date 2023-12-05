try:
    import logging
    import os
    import timeit

except:
    print("Imports failed")

TEST = not True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

class Map:
    def __init__(self,map_details, max_source):
        
        self.source_txt,\
            self.dest_text = self.get_source_dest(map_details)

        self.max_source = max_source
        self.map_dict = self.create_map(map_details) #key=source: val=destination
        

    def get_source_dest(self,details):
        hyphenated = details[0]
        hyphenated = hyphenated.split(" ")
        source = hyphenated[0].split("-")[0]
        dest = hyphenated[0].split("-")[2]

        return source, dest


    def create_map(self, details):
        map_dict = {}
        ranges = details[1:]
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

                if source > self.max_source:
                    self.max_source = source

        #map_dict_sorted = dict(sorted(map_dict.items()))

        #fill in the gaps:
        # for j in range(0, self.max_source):
        #     if j in map_dict.keys():
        #         pass
        #     else:
        #         map_dict[j] = j

        return map_dict


    def follow(self, source):
        if source in self.map_dict.keys():
            return self.map_dict[source]
        else:
            return source

    def __repr__(self):
        str = "Map {} to {} ".format(self.source_txt, self.dest_text)
        return(str)

    def __str__(self):
        return(self.__repr__())



class Seed:
    def __init__(self, seed_num, map_list):
        
        self.details = [None]*8

        self.seed = seed_num
        self.details[0] = self.seed
        # self.soil = None
        # self.fert = None
        # self.water = None

        # self.light = None
        # self.temp = None
        # self.humid = None
        # self.loc = None

        self.follow_maps(map_list)
        self.loc = self.details[-1]
        

    def follow_maps(self, map_list):
        for i in range(0,len(self.details)-1):
            self.details[i+1] = map_list[i].follow(source = self.details[i])


    def __repr__(self):
        str = "Seed{}".format(self.seed)
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
    main_max_source = 0

    for i, map in enumerate(maps_input):
        new_map = Map(map, main_max_source)
        map_list.append(new_map)
        
        if new_map.max_source > main_max_source:
            #print("New bigger value of source")
            main_max_source = new_map.max_source

    #parse input and create seeds
    seed_numbers = seeds_input[0]
    seed_numbers = seed_numbers.split(":")[1]
    seeds_list = seed_numbers.split()

    for i, seed in enumerate(seeds_list):
        seed_list.append(Seed(int(seed), map_list))

    smallest_loc = 0
    closest_seed = None
    for i, seed in enumerate(seed_list):
        if i == 0:
            smallest_loc = seed.loc
            closest_seed = seed
        else:
            if seed.loc < smallest_loc:
                smallest_loc = seed.loc
                closest_seed = seed
    
    print(closest_seed)
    print(smallest_loc)
        
        
    


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))