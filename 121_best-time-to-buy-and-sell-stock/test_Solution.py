from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_max_profit(self):
        self.assertEqual(5, Solution().maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, Solution().maxProfit([7, 6, 4, 3, 1]))
        self.assertEqual(93, Solution().maxProfit([7, 100, 4, 3, 1]))
        self.assertEqual(2, Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]))
        self.assertEqual(4, Solution().maxProfit([3, 2, 6, 5, 0, 3]))
