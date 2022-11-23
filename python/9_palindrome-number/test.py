import unittest

from Solution import Solution


class MyTestcase(unittest.TestCase):
    def test(self):
        self.assertTrue(Solution().isPalindrome(123321))
        self.assertTrue(Solution().isPalindrome(12321))
        self.assertTrue(Solution().isPalindrome(1))
        self.assertFalse(Solution().isPalindrome(10))
        self.assertFalse(Solution().isPalindrome(-121))


if __name__ == '__main__':
    unittest.main()
