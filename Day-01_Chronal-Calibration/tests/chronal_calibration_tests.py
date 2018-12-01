import sys
sys.path.insert(0, '..')
import chronal_calibration as cc



def chronal_calibration_tests():

    assert cc.chronal_calibration('cc-pt1_test-1.txt') == 3, "part 1 test 1 failed"
    assert cc.chronal_calibration('cc-pt1_test-2.txt') == 0, "part 1 test 2 failed"
    assert cc.chronal_calibration('cc-pt1_test-3.txt') == -6, "part 1 test 3 failed"



if __name__ == '__main__':

    chronal_calibration_tests()


