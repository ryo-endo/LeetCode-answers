from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_get_row(self):
        self.assertEqual([1, 3, 3, 1], Solution().getRow(3))
