import sys
sys.path.insert(0, '..')
import repose_record as rr



def template_tests():

    assert rr.most_minutes_asleep('rr-pt1_test-1.txt') == 240, "part 1 test 1 failed"



if __name__ == '__main__':

    template_tests()


