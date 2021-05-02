from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_max_sub_array(self):
        self.assertEqual(6, Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
