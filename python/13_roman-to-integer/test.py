import unittest

from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, Solution().romanToInt('I'))
        self.assertEqual(3, Solution().romanToInt('III'))
        self.assertEqual(4, Solution().romanToInt('IV'))
        self.assertEqual(1994, Solution().romanToInt('MCMXCIV'))


if __name__ == '__main__':
    unittest.main()
