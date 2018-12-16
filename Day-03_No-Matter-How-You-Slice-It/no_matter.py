import numpy as np
import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    lines = [parse_input_line(l) for l in lines]
    
    return(lines)



def parse_input_line(line):

    x = line.split(' ')

    id = int(x[0].replace('#', ''))

    dist_to_left = int(x[2].split(',')[0])

    dist_to_top = int(x[2].split(',')[1].replace(':', ''))

    width = int(x[3].split('x')[0])

    height = int(x[3].split('x')[1])

    return([id, dist_to_left, dist_to_top, width, height])




def count_gird_square_claims(file):
    """Count the number of times each grid square is used (claimed)"""

    squares = read_input(file)

    # list to hold results
    counts = np.array([0] * (1000 * 1000))

    for sq in squares:

        start_stop_list = coords_to_squares(sq[1], sq[2], sq[3], sq[4])

        for pair in start_stop_list:

            counts[pair[0]:pair[1]] = counts[pair[0]:pair[1]] + 1

    # count the number of squares with 2 or more claims
    two_count = np.sum(counts >= 2)

    return(two_count)



def coords_to_squares(dist_to_left, dist_to_top, width, height):
    """Function to convert 4 'coordinates' i.e. distance to top & left, height and width 
    to start and end values for the squares covered by these particular coordinates. 
    Values """

    start_stop_pairs = []

    # loop through each row of the square
    for row in range(height):

        start_stop_pairs.append(((dist_to_top + row) * 1000 + dist_to_left, (dist_to_top + row) * 1000 + dist_to_left + width))

    return(start_stop_pairs)


if __name__ == '__main__':

    a = count_gird_square_claims(sys.argv[1])

    print(a)

