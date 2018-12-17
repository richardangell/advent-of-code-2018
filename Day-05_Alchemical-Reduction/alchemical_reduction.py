import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    lines = lines[0][:(len(lines[0])-1)]

    return(lines)



def alchemical_reduction(file):

    polymer = read_input(file)

    polymer_list = list(polymer)

    # add item to end so we know where the end of the list is
    polymer_list.append('1')

    i = 0

    # loop through all elements in the list from start to finish (left to right in the string)
    while True:
        
        #print(i)

        # if we get to the end of the list then break
        if polymer_list[i] == '1':

            break

        if polymer_list[i].upper() == polymer_list[i]:

            i_upper = True
        
        else:

            i_upper = False

        if polymer_list[i+1].upper() == polymer_list[i+1]:

            i_plus_1_upper = True
        
        else:

            i_plus_1_upper = False
        
        if polymer_list[i].upper() == polymer_list[i+1].upper():

            match_next_letter = True

        else:

            match_next_letter = False

        if (i_upper & (not i_plus_1_upper)) or ((not i_upper) & i_plus_1_upper):

            case_not_match = True
            
        else:

            case_not_match = False

        # compare the current letter to the next 
        # if they are the same letter but not the same case then remove both from the list
        # note decrease counter here as the previous letter might now match to the new one next to it
        if match_next_letter & case_not_match:
            
            del polymer_list[i+1]

            del polymer_list[i]

            i -= 1

            # stop the index going negative
            i = max(0, i)

        # otherwise delete neither and move onto next pair
        else:

            i += 1

    # answer is -1 as we added an extra element to the end
    print(len(polymer_list) - 1)

    return(len(polymer_list) - 1)



if __name__ == '__main__':

    alchemical_reduction(sys.argv[1])

