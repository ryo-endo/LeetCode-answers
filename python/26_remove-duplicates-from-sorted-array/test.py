import unittest

from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([1, 2, 3, 4], Solution().removeDuplicates([1, 1, 2, 3, 3, 4]))


if __name__ == '__main__':
    unittest.main()
