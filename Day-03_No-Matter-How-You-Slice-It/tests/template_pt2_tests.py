import sys
sys.path.insert(0, '..')
import no_matter_pt2 as nm_pt2



def template_tests_pt2():

    assert nm_pt2.count_gird_square_claims('nm-pt1_test-1.txt') == 3, "part 2 test 1 failed"



if __name__ == '__main__':

    template_tests_pt2()

