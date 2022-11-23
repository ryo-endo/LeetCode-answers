import unittest

from Solution import Solution, ListNode


class MyTestCase(unittest.TestCase):
    def test_something(self):
        n2 = ListNode(2)
        n1 = ListNode(1, n2)
        m2 = ListNode(2)
        m1 = ListNode(1, m2)

        self.assertEqual('1122', self.NodeListStr(Solution().mergeTwoLists(n1, m1)))
        self.assertEqual(None, Solution().mergeTwoLists(None, None))

    def NodeListStr(self, node: ListNode):
        str = ''
        node = node
        while node != None:
            str += repr(node)
            node = node.next
        return str


if __name__ == '__main__':
    unittest.main()
