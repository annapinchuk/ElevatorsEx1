import unittest
import main
from callforelevator import callforelevator
from building import building
from elevator import elevator


class elev_test_main(unittest.TestCase):

    def test_allocate_call_for_elev(self):

        first_call = callforelevator(13, 2, 1, 3, -1)  # call of length 1
        sec_call = callforelevator(20, 9, 2, 3, -1)  # call of length 7
        first_elev = elevator(0, 0, 10, 10, 2, 2, 3, 3)  # fastest elevator
        sec_elev = elevator(1, 0, 10, 10, 2, 2, 3, 3)  # slowest elevator
        third_elev = elevator(2, 0, 10, 10, 2, 2, 3, 3)  # second fastest elevator
        building_ = building([first_elev, sec_elev, third_elev], 0, 10)
        first_call = main.allocate_call_for_elev(first_call, 10, building_)
        sec_call = main.allocate_call_for_elev(sec_call, 10, building_)

        self.assertEqual(first_call.elev, 0)
        self.assertEqual(sec_call.elev, 1)
