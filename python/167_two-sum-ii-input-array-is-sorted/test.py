import unittest

from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([1, 2], Solution().twoSum([2, 7, 11, 15], 9))
        self.assertEqual([1, 3], Solution().twoSum([2, 3, 4], 6))
        self.assertEqual([1, 2], Solution().twoSum([-1, 0], -1))


if __name__ == '__main__':
    unittest.main()
