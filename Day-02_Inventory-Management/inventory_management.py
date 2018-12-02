import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    return(lines)



def inventory_management(file):

    f = read_input(file)

    twos = []

    threes = []

    for x in f:

        x_list = list(x)

        x_set = set(x_list)

        x_twos = []

        x_threes = []

        for x_letter in x_set:

            x_letter_count = x_list.count(x_letter)

            if x_letter_count == 2:

                x_twos.append(x_letter)

            elif x_letter_count == 3:
                
                x_threes.append(x_letter)

        twos.append(len(x_twos))

        threes.append(len(x_threes))

    twos_count = len([j for j in twos if j > 0])
    
    threes_count = len([j for j in threes if j > 0])

    print(twos_count, threes_count, twos_count * threes_count)

    return(twos_count, threes_count, twos_count * threes_count)




if __name__ == '__main__':

    inventory_management(sys.argv[1])

