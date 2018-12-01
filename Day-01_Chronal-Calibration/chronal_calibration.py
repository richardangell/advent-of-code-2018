import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        lines[i] = int(lines[i])

    return(lines)



def chronal_calibration(file):

    f = read_input(file)

    resulting_frequency = sum(f)

    print(resulting_frequency)

    return(resulting_frequency)




if __name__ == '__main__':

    chronal_calibration(sys.argv[1])

