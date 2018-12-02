import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    return(lines)



def template_pt2(file):

    f = read_input(file)




if __name__ == '__main__':

    template_pt2(sys.argv[1])

