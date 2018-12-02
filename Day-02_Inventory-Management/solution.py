import chronal_calibration as cc
import chronal_calibration_pt2 as cc_pt2

if __name__ == '__main__':

    file = "inputs.txt"

    cc.chronal_calibration(file)

    cc_pt2.chronal_calibration_pt2(file)
