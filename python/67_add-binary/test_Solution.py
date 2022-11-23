from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_add_binary(self):
        self.assertEqual("100", Solution().addBinary('11','1'))


