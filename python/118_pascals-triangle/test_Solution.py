from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_generate(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], Solution().generate(5))
        self.assertEqual([[1]], Solution().generate(1))
