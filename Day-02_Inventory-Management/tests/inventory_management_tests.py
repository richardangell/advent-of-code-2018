import sys
sys.path.insert(0, '..')
import inventory_management as im



def inventory_management_tests():

    twos, threes, result = im.inventory_management('im-pt1_test-1.txt') 

    assert twos == 4, "part 1 test 1 failed: twos"
    assert threes == 3, "part 1 test 1 failed: threes"
    assert result == 12, "part 1 test 1 failed: result"


if __name__ == '__main__':

    inventory_management_tests()


