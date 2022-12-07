try:
    import logging
    import os

except:
    print("Imports failed")

TEST = not True

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
    def __repr__(self):
        return str(self.name)

    def __init__(self, name, parent_dir):
        self.name = name
        self.parent_dir = parent_dir

        self.files = []
        self.files_size = 0 # total

        self.sub_dirs = []
        self.sub_dir_size = 0 #total size of sub directories

        self.this_dir_total_size = 0#total 

    def add_file(self, file_to_add):
        self.files.append(file_to_add)

    def add_sub_dir(self, dir_to_add):
        self.sub_dirs.append(dir_to_add)

    def get_total_files_size(self): # for only this directory and not sub directories
        total = 0
        
        for i, fileObj in enumerate(self.files):
             total += fileObj.size

        self.files_size = total
        self.update_this_dir_size()
        
    def get_size_all_subdir(self):
        total = 0

        for i, subdirObj in enumerate(self.sub_dirs):
            total += subdirObj.this_dir_total_size

        self.sub_dir_size = total
        self.update_this_dir_size()

    def update_this_dir_size(self):
        self.this_dir_total_size = self.files_size + self.sub_dir_size

    def dir_contents(self):
        buf = []
        buf.append(self.sub_dirs)
        buf.append(self.files)
        return buf.copy()

class File():


    def __init__(self, name, size, parent_dir):
        self.name = name
        self.size = size
        self.parent_dir = parent_dir

    def __repr__(self):
        return str(self.name + " " +str(self.size))

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
                        file = File(tmp[1],int(tmp[0]), cwd)
                        cwd.add_file(file)
                        cwd.get_total_files_size()

            elif line[1] == 'cd':
                cwd.get_size_all_subdir()
                if line[2] == '..':
                    next_dir = cwd.parent_dir
                    cwd = next_dir
                    i_next = i+1
                else:
                    next_dir_name = line[2]
                    next_dir = find_sub_dir(next_dir_name,cwd.sub_dirs)
                    cwd = next_dir
                    i_next = i+1

        root.get_total_files_size()
        root.get_size_all_subdir()
        root.update_this_dir_size()            
        i = i_next

    return root

def find_sub_dir(dir_name, sub_dirs_list):

    for i, value in enumerate(sub_dirs_list):
        if value.name == dir_name:
            return  value
        else:
            #logging.error("didnt find that directory")
            continue


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

    return list_files_dirs, j+1

def find_all(root):
    dirs = root.sub_dirs
    buf = []
    for i, dir in enumerate(dirs):
        if dir.sub_dirs:
            buf.append(find_all(dir))
        else:
            return dir
    



def main():

    input = get_input()
    root = parse(input)
    #print(root.this_dir_total_size)

    #traverse tree, check each total size is < 100000
    """
    function findInputFiles(workDirectory) {
	list = getFileList(workDirectory);
	
	for (i=0; i<list.length; i++) {
		if (endsWith(list[i], "/"))
			findInputFiles(workDirectory+list[i]);
		else if (endsWith(list[i], ".avi"))
			runAnalysis(workDirectory+list[i]);
		}
    }
    """
    full_dir_list = []
    for i, dir in enumerate(root.sub_dirs):
        full_dir_list.append(dir)
        if dir.sub_dirs:
            full_dir_list.append(find_all(dir))
        else:
            continue

    sum = 0

    for i, dir in enumerate(full_dir_list):
        if dir.this_dir_total_size <= 100000:
            sum += dir.this_dir_total_size
        else:
            continue
    
    print(sum)
    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")