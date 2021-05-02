from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_str_str(self):
        self.assertEqual(2, Solution().strStr('hello', 'll'))
        self.assertEqual(-1, Solution().strStr('hello', 'a'))
        self.assertEqual(0, Solution().strStr('', ''))
