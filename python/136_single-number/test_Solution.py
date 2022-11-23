from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_single_number(self):
        self.assertEqual(1, Solution().singleNumber([2, 2, 1]))
        self.assertEqual(4, Solution().singleNumber([4, 1, 2, 1, 2]))
        self.assertEqual(1, Solution().singleNumber([1]))
