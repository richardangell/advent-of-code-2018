import sys
sys.path.insert(0, '..')
import alchemical_reduction as al



def template_tests():

    assert al.alchemical_reduction('pt1_test1.txt') == 10, "part 1 test 1 failed"



if __name__ == '__main__':

    template_tests()


