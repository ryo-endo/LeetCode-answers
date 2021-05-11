from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_is_palindrome(self):
        self.assertEqual(True, Solution().isPalindrome("A man, a plan, a canal: Panama"))
        self.assertEqual(False, Solution().isPalindrome("0P"))
