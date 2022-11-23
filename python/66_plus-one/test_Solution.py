from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_plus_one(self):
        self.assertEqual([1,2,3,5], Solution().plusOne([1,2,3,4]))
