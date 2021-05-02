from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_merge(self):
        l1 = [1, 2, 3, 0, 0, 0]
        l2 = [2, 5, 6]
        Solution().merge(l1, 3, l2, 3)
        self.assertEqual([1, 2, 2, 3, 5, 6], l1)
