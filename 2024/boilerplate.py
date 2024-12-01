try:
    import logging
    import os
    import shutil
    #from git import *
    from pathlib import Path

except:
    print("Imports failed")

YEAR = 2024
DAY = "Day"
TEST_INPUT = "test_input.txt"
INPUT = "input.txt"

def main():
    #take in day number
    #n = user input
    while True:
        try:
            n = int(input("Enter day number:"))
        except ValueError:
            print("Please, enter a valid integer")
            continue
        else:
            print("Creating... Year {}, Day {}".format(YEAR, n))
            break

    #create folder/ folder structure   
    folder_name = DAY + str(n)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    folder_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), folder_name)

    try:
        os.mkdir(folder_dir)
    except FileExistsError:
        print("Folder already exists")

    #create 2x python files with basic code in #where does the code come from #write the day on top?
    template_name = os.path.join(current_dir,"template.py")
    part_1_title = DAY + str(n) +".py"
    shutil.copyfile(template_name, os.path.join(folder_dir, part_1_title))

    part_2_title = DAY + str(n) +"_2.py"
    shutil.copyfile(template_name, os.path.join(folder_dir, part_2_title))

    p = Path(os.path.dirname(os.path.realpath(__file__)))
    git_repo_path = p.parent
    
    
    # repo = Repo(git_repo_path)
    # #repo.index.add(folder_dir)
    # repo.index.add(folder_dir)
    # repo.index.commit("Auto adding files for Day " + str(n))
    
    # origin = repo.remote('origin')
    # origin.push()
    
    #create input.txt
    with open(os.path.join(folder_dir, INPUT),'w') as f:
        pass

    #create test_input.txt
    with open(os.path.join(folder_dir, TEST_INPUT),'w') as f:
        pass

    print("done")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")