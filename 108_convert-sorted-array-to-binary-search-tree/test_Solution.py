from unittest import TestCase

from Solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_sorted_array_to_bst(self):
        self.assertEqual([0, -3, 9, -10, None, 5, None],
                         self.TreeNodeToList(Solution().sortedArrayToBST([-10, -3, 0, 5, 9])))
        self.assertEqual([3, 1, None],
                         self.TreeNodeToList(Solution().sortedArrayToBST([1, 3])))

    def TreeNodeToList(self, root: TreeNode):
        l = []

        def appendNode(node: TreeNode):
            if not node or (not node.left and not node.right):
                return

            if node.left:
                l.append(node.left.val)
            else:
                l.append(None)

            if node.right:
                l.append(node.right.val)
            else:
                l.append(None)

            appendNode(node.left)
            appendNode(node.right)

        l.append(root.val)
        appendNode(root)

        return l
