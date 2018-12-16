import sys
sys.path.insert(0, '..')
import no_matter as nm



def template_tests():

    assert nm.count_gird_square_claims('nm-pt1_test-1.txt') == 4, "part 1 test 1 failed"



if __name__ == '__main__':

    template_tests()


