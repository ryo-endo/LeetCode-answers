import unittest

from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('fl', Solution().longestCommonPrefix(["flower","flow","flight"]))
        self.assertEqual('flower', Solution().longestCommonPrefix(["flower","flowers","flowerss"]))
        self.assertEqual('flower', Solution().longestCommonPrefix(["flowers","flower","flowerss"]))
        self.assertEqual('', Solution().longestCommonPrefix(["dog","racecar","car"]))


if __name__ == '__main__':
    unittest.main()
