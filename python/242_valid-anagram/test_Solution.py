import unittest
from Solution import Solution

"""
- [x] 同じ並び順の文字列のときにはTrueを返す
- [x] 異なる文字列だが同じアルファベットで構成されているならTrueを返す
- [x] 異なる文字列で構成するアルファベットも異なるならFalseを返す
"""


class ValidAnagram(unittest.TestCase):
    def test_同じ文字列のときにはTrueを返す(self):
        self.assertTrue(Solution().isAnagram('ab', 'ab'))

    def test_文字数が異なる場合はFalseを返す(self):
        self.assertFalse(Solution().isAnagram('ab', 'abb'))

    def test_異なる文字列だが同じアルファベットで構成されているならTrueを返す(self):
        self.assertTrue(Solution().isAnagram('anagram', 'nagaram'))

    def test_異なる文字列で構成するアルファベットも異なるならFalseを返す(self):
        self.assertFalse(Solution().isAnagram('rat', 'car'))


if __name__ == '__main__':
    unittest.main()
