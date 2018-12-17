import sys
sys.path.insert(0, '..')
import repose_record_pt2 as rr_pt2



def template_tests():

    assert rr_pt2.most_minutes_asleep('rr-pt1_test-1.txt') == 4455, "part 2 test 1 failed"



if __name__ == '__main__':

    template_tests()


