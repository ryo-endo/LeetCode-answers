from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_climb_stairs(self):
        self.assertEqual(1, Solution().climbStairs(1))
        self.assertEqual(2, Solution().climbStairs(2))
        self.assertEqual(3, Solution().climbStairs(3))
        self.assertEqual(5, Solution().climbStairs(4))