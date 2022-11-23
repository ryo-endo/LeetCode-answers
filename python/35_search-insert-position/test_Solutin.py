from unittest import TestCase

from Solutin import Solution


class TestSolution(TestCase):
    def test_search_insert(self):
        self.assertEqual(2, Solution().searchInsert([1,3,5,6], 5))
        self.assertEqual(4, Solution().searchInsert([1,3,5,6], 7))
