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

    # list to hold ids
    ids = np.array([np.NaN] * (1000 * 1000))

    for sq in squares:

        start_stop_list = coords_to_squares(sq[1], sq[2], sq[3], sq[4])

        for pair in start_stop_list:

            counts[pair[0]:pair[1]] = counts[pair[0]:pair[1]] + 1

            # note this will overwrite ids if count > 1
            ids[pair[0]:pair[1]] = sq[0]

    #print(counts[:10])
    #print(counts[1000:1010])
    #print(counts[2000:2010])
    #print(counts[3000:3010])
    #print(counts[4000:4010])
    #print(counts[5000:5010])
    #print(counts[6000:6010])
    #print(counts[7000:7010])
    #print(counts[8000:8010])

    #print(ids[:10])
    #print(ids[1000:1010])
    #print(ids[2000:2010])
    #print(ids[3000:3010])
    #print(ids[4000:4010])
    #print(ids[5000:5010])
    #print(ids[6000:6010])
    #print(ids[7000:7010])
    #print(ids[8000:8010])

    # get the ids of the squares with no overlaps 
    # note this will include squares that do overlap
    non_overlapping_squares = np.unique(ids[np.where(counts == 1)])

    # loop through each of the identified squares and determine which squares they cover
    # then check if the squares overlap with anything else
    for id in non_overlapping_squares:

        sq = squares[int(id)-1]

        # reculate the start stop list
        # note efficient but easier than keeping track of all the ids used in a given square
        start_stop_list = coords_to_squares(sq[1], sq[2], sq[3], sq[4])

        for pair in start_stop_list:

            # note this will overwrite ids
            ids[pair[0]:pair[1]] = sq[0]

        # now check counts for this particular id after we have overwritten the ids in ids
        if np.all(counts[np.where(ids == sq[0])] == 1):
            
            return(sq[0])



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

