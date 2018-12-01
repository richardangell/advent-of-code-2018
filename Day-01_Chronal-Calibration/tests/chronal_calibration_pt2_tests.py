import sys
sys.path.insert(0, '..')
import chronal_calibration_pt2 as cc



def chronal_calibration_pt2_tests():

    assert cc.chronal_calibration_pt2('cc-pt2_test-1.txt') == 0, "part 1 test 1 failed"
    assert cc.chronal_calibration_pt2('cc-pt2_test-2.txt') == 10, "part 1 test 2 failed"
    assert cc.chronal_calibration_pt2('cc-pt2_test-3.txt') == 5, "part 1 test 3 failed"
    assert cc.chronal_calibration_pt2('cc-pt2_test-4.txt') == 14, "part 1 test 4 failed"


if __name__ == '__main__':

    chronal_calibration_pt2_tests()


