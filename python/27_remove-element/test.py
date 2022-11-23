import unittest

from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [3, 2, 2, 3]
        self.assertEqual(2, Solution().removeElement(nums, 3))
        self.assertEqual([2, 2], nums)


if __name__ == '__main__':
    unittest.main()
