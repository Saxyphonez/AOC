try:
    import logging
    import os
    import timeit
    import re
    import numpy as np

except:
    print("Imports failed")

TEST = not True

if TEST:
    input_filename = "test_input.txt"
else:
    input_filename = "input.txt"
    

def get_input():
    input = []

    input_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_filename)
    #print(input_filepath)

    with open(input_filepath,'r') as f:
        input = f.readlines()

    #probably an easier way to do this but leave me alone, ok
    input = [line.strip() for line in input]
    input = [x.split() for x in input]

    for i,line in enumerate(input):
        input[i] = [int(x) for x in line]

    return input

def do_maths_clever(seq):
    next_in_seq = None

    diff_seq_list = []
    count = 0
    diff_seq_list.append(seq.copy())

    #while differeces not all 0
    while not(diff_seq_list[count].count(0) == len(diff_seq_list[count])): 
        diff_seq_list.append(get_diff_list(diff_seq_list[count]))
        count += 1

    poly_degree_n = count -1 #degree of nth term sequence polynomial
    print("order {} polynomial".format(poly_degree_n))

    A = []

    for i in range(1, len(seq)+1):
        buf = []

        for a in range(0, poly_degree_n+1):
            buf.append(pow(i,a))

        A.append(buf)

    #coefs = inv(A)*seq
    A_mat = np.array(A[0:poly_degree_n+1])
    A_mat = A_mat.astype(np.float64)

    seq_mat = np.array(seq[0:poly_degree_n+1])

    coefs_mat = np.linalg.solve(A_mat, seq_mat)

    coefs = list(coefs_mat)

    next_in_seq = 0

    for x in range(0, len(coefs)):
        next_in_seq += coefs[x]*(pow((len(seq)+1),x))

    print(next_in_seq)
    return next_in_seq


def do_maths(seq):
    next_in_seq = None

    diff_seq_list = []
    count = 0
    diff_seq_list.append(seq.copy())

    #while differeces not all 0
    while not(diff_seq_list[count].count(0) == len(diff_seq_list[count])): 
        diff_seq_list.append(get_diff_list(diff_seq_list[count]))
        count += 1

    # poly_degree_n = count -1 #degree of nth term sequence polynomial
    # print("order {} polynomial".format(poly_degree_n))

    #work backwards:
    #next_in_seq = find_next(diff_seq_list)
    next_in_seq = find_prev(diff_seq_list)

    return next_in_seq

def find_next(seq_lst):
    lst = seq_lst.copy()
    lst.reverse()

    for i, line in enumerate(lst):
        if i == 0 :
            line.append(0)
        else:
            line.append(line[-1]+lst[i-1][-1])
    return lst[-1][-1]

def find_prev(seq_lst):
    lst = seq_lst.copy()
    lst.reverse()

    for i, line in enumerate(lst):
        if i == 0 :
            line.append(0)
        else:
            line.append(line[0]-lst[i-1][-1])

    if TEST:
        print(lst[-1][-1])
    return lst[-1][-1]



def get_diff_list(seq):
    lst = []
    for i in range(0, len(seq)-1):
        lst.append(seq[i+1]-seq[i])

    return lst

def main():
    data = get_input()
    total = 0

    for seq in data:
        total += do_maths(seq)
        #total += do_maths_clever(seq)

    print(round(total))
    print("done")


if __name__ == "__main__":
    try:
        #total_time = timeit.timeit('main', number=1, globals=globals())
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")

    #print('Average time: {} usec'.format((total_time/1)*1e6))