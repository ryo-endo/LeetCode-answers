import unittest

from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertTrue(Solution().isValid('()'))
        self.assertTrue(Solution().isValid('({[]})'))
        self.assertTrue(Solution().isValid('{}'))
        self.assertTrue(Solution().isValid('[]'))
        self.assertTrue(Solution().isValid('()[]{}'))

        self.assertFalse(Solution().isValid('['))
        self.assertFalse(Solution().isValid(']'))
        self.assertFalse(Solution().isValid('(]'))
        self.assertFalse(Solution().isValid('([)]'))


if __name__ == '__main__':
    unittest.main()
