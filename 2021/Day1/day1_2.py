try:
    import logging
    import os
except:
    print("Imports failed")



def get_input():
    input_filepath = os.getcwd() + "\\2021\\Day1\\"+ "input.txt"

    with open(input_filepath,'r') as f:
        measurements = f.readlines()

    f.close()

    for i in range(len(measurements)):
        measurements[i] = int(measurements[i])

    return measurements

def main():
    increase_count = 0
    measurements = get_input()
    #measurements = [199,200,208,210,200,207,240,269,260,263]
    previous_avg = 0

    for i in range(len(measurements)):
        if i == 0 :
            current_avg = measurements [i] + measurements[i+1] + measurements[i+2]
            #print(current_avg)
            previous_avg = current_avg
            continue

        else:
            if i+2 <= len(measurements)-1 :
                current_avg = measurements [i] + measurements[i+1] + measurements[i+2]
                #print(current_avg)
                #print(previous_avg)

                if current_avg > previous_avg:
                    print(str(current_avg) + " " + str(previous_avg))
                    increase_count += 1
                    previous_avg = current_avg
                    continue

                else:
                    previous_avg = current_avg
                    continue

            else:
                print(i)
                break
        #save as previous avg

    print("Number of increases: " + str(increase_count))



if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("KB interrupt detected")


