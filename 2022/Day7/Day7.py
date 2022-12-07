try:
    import logging
    import os

except:
    print("Imports failed")

TEST = True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"

"""
TODO:
parse the input
somehow traverse my structure



DONE:
create an object for a directory containing:
- list of files + list of file sizes in one list
- list of subdirectory as objects + sum of sub dir files

- total sum of directory's files
- total sum of dir's sub dirs

- sum of those sums
- function to add a dir/file to the lists

"""

class Directory():
    files = []
    files_size = 0 # total

    sub_dirs = []
    sub_dir_size = 0 #total size of sub directories

    this_dir_total_size = 0#total 

    parent_dir = None

    def __init__(self, name, parent_dir):
        self.name = name
        self.parent_dir = parent_dir

    def add_file(self, file_to_add):
        self.files.append(file_to_add)
        self.update_files_size(file_to_add[0])
        self.update_total_dir_size()

    def add_sub_dir(self, dir_to_add):
        self.files.append(dir_to_add)
        self.update_subdir_size()

    def update_files_size(self, size_to_add):
        self.files_size += size_to_add

    def update_subdir_size(self):
        total = 0
        for i, value in enumerate(self.sub_dirs):
            total += value.files_size

        self.sub_dir_size = total

    def update_total_dir_size(self):
        self.this_dir_total_size = self.files_size + self.sub_dir_size


def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    input = [x.strip("\n") for x in input]

    return input


def parse(input):
    root = Directory("/", None)
    i = 1
    cwd = root
    while(i<len(input)):

        line = input[i].split(" ")

        if line[0] == '$':
            if line [1] == 'ls':
                list_dir, i_next = collect_useful_lines(input,i)

                for j, value in enumerate(list_dir):
                    tmp = value.split(" ")

                    if tmp[0] == 'dir':
                        new_sub_dir = Directory(tmp[1], cwd)
                        cwd.add_sub_dir(new_sub_dir)

                    elif tmp[0] != 'dir':
                        cwd.add_file(tmp)

            elif line[1] == 'cd':
                if line[2] == '..':
                    next_dir = cwd.parent_dir
                    cwd = next_dir
                else:
                    #find that dir object
                    #change to that dir
                    pass
                    


    i = i_next



    return root


def collect_useful_lines(input, i):
    #start at input[i+1]
    #find the next $ sign
    #return list of files/dirs, index of next dollar sign
    list_files_dirs = []
    next_dollar_index = i

    for j in range(i+1, len(input)):
        if "$" in input[j]:
            next_dollar_index = j
            return list_files_dirs,j

        else:
            list_files_dirs.append(input[j])

    #return list_files_dirs, j+1



def main():

    input = get_input()
    root = parse(input)
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")