import unittest

from Solution import Solution, ListNode


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('12', self.NodeListStr(Solution().deleteDuplicates(self.create_node([1, 1, 2]))))
        self.assertEqual('123', self.NodeListStr(Solution().deleteDuplicates(self.create_node([1, 1, 2,3,3]))))
        self.assertEqual('', self.NodeListStr(Solution().deleteDuplicates(None)))

    @staticmethod
    def NodeListStr(node: ListNode):
        str = ''
        if not node:
            return str

        node = node
        while node is not None:
            str += repr(node)
            node = node.next
        return str

    @staticmethod
    def create_node(nums: list) -> ListNode:
        top = cur = ListNode(nums[0])
        for n in nums[1:]:
            cur.next = ListNode(n)
            cur = cur.next

        return top


if __name__ == '__main__':
    unittest.main()
