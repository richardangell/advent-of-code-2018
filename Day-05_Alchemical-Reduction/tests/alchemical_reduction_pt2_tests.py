import sys
sys.path.insert(0, '..')
import alchemical_reduction_pt2 as al2



def template_tests():

    assert al2.alchemical_reduction_better('pt1_test1.txt') == 4, "part 2 test 1 failed"



if __name__ == '__main__':

    template_tests()


