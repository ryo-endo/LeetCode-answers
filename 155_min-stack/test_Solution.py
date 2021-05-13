from unittest import TestCase

from Solution import MinStack


class TestMinStack(TestCase):
    def test_minStack(self):
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        self.assertEqual(-3, ms.getMin())
        ms.pop()
        self.assertEqual(0, ms.top())
        self.assertEqual(-2, ms.getMin())

    def test_minStack2(self):
        ms = MinStack()
        ms.push(-1)
        self.assertEqual(-1, ms.top())
        self.assertEqual(-1, ms.getMin())

    def test_empty(self):
        ms = MinStack()
        ms.pop()
        ms.top()
        ms.getMin()
