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
        
        self.source_txt,\
            self.dest_text = self.get_source_dest(map_details)

        self.range_list = self.create_range_list(map_details)
        

    def get_source_dest(self,details): #text
        hyphenated = details[0]
        hyphenated = hyphenated.split(" ")
        source = hyphenated[0].split("-")[0]
        dest = hyphenated[0].split("-")[2]

        return source, dest


    def create_range_list(self, details):
        buf = []

        for item in details[1:]:
            num = item.split()
            num = [int(x) for x in num]
            buf.append(num)

        return buf

    def follow(self, source):
        dest = None

        for rang in self.range_list: #range cos range is keyword
            source_range_start = rang[1]
            range_len = rang[2]
            dest_range_start = rang[0]

            if source >= source_range_start and source <= source_range_start+range_len:
                diff_src = source - source_range_start
                dest = dest_range_start + diff_src
            else:
                continue
        
        if dest == None:
            dest = source
        
        return dest

    def __repr__(self):
        str = "Map: {} to {} ".format(self.source_txt, self.dest_text)
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
    seed_obj_list = []

    for i, map in enumerate(maps_input):
        new_map = Map(map)
        map_list.append(new_map)



    #parse input and create seeds
    seed_numbers = seeds_input[0]
    seed_numbers = seed_numbers.split(":")[1]
    seeds_list = seed_numbers.split()

    for i, seed in enumerate(seeds_list):
        seed_obj_list.append(Seed(int(seed), map_list))

    smallest_loc = 0
    closest_seed = None
    for i, seed in enumerate(seed_obj_list):
        if i == 0:
            smallest_loc = seed.loc
            closest_seed = seed
        else:
            if seed.loc < smallest_loc:
                smallest_loc = seed.loc
                closest_seed = seed
    
    print(closest_seed)
    print(smallest_loc)
    print("done")
        
        
    


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))