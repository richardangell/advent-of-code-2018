import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    return(lines)



def template(file):

    f = read_input(file)





if __name__ == '__main__':

    template(sys.argv[1])

