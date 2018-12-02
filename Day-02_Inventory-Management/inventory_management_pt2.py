import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    return(lines)



def inventory_management_pt2(file):

    f = read_input(file)

    first, second = loop_compare(f)

    common_letters = []

    first_list = list(first)

    second_list = list(second)

    for first_char, second_char in zip(first_list, second_list):

        if first_char == second_char:

            common_letters.append(first_char)

    common_letters.pop()

    common_letters = ''.join(common_letters)

    print(common_letters)

    return(common_letters)


def loop_compare(f):

    n = len(f)

    for i in range(n):

        for j in range(n):

            if i != j:
                
                differences = compare_two_strings(f[i], f[j])

                if differences == 1:
                    
                    print(f[i], f[j], differences)

                    return(f[i], f[j])




def compare_two_strings(s1, s2):

    s1_list = list(s1)

    s2_list = list(s2)

    differences_count = 0

    for s1_char, s2_char in zip(s1_list, s2_list):

        if s1_char != s2_char:

            differences_count += 1

    return(differences_count)


if __name__ == '__main__':

    inventory_management_pt2(sys.argv[1])

