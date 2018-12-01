import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        lines[i] = int(lines[i])

    return(lines)



def chronal_calibration_pt2(file):

    f = read_input(file)

    n = len(f)

    resulting_frequencies = [0]

    i = 0

    j = 0

    while True:
      
        new_frequency = resulting_frequencies[-1] + f[i]

        if new_frequency in resulting_frequencies:

            print(new_frequency)
            
            return(new_frequency)

        else:

            resulting_frequencies.append(new_frequency)

        i += 1

        # if i gets bigger than the length of the input reset to 0
        if i == n:

            i = 0

            j += 1

            print('reset loop', j)





if __name__ == '__main__':

    chronal_calibration_pt2(sys.argv[1])

