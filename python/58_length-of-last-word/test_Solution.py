from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_length_of_last_word(self):
        self.assertEqual(5, Solution().lengthOfLastWord("Hello World"))
        self.assertEqual(0, Solution().lengthOfLastWord("       "))
        self.assertEqual(2, Solution().lengthOfLastWord("aa"))
        self.assertEqual(1, Solution().lengthOfLastWord(" a"))
        self.assertEqual(1, Solution().lengthOfLastWord("a "))

