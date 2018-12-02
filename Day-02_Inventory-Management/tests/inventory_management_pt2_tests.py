import sys
sys.path.insert(0, '..')
import inventory_management_pt2 as im2



def inventory_management_pt2_tests():

    assert im2.inventory_management_pt2('im-pt2_test-1.txt') == 'fgij', "part 1 test 1 failed"



if __name__ == '__main__':

    inventory_management_pt2_tests()


