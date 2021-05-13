from unittest import TestCase

from Solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_preorder_traversal(self):
        self.assertEqual([1, 2, 3], Solution().preorderTraversal(
            TreeNode(1,
                     None,
                     TreeNode(2,
                              TreeNode(3),
                              None)
                     )
        ))

        self.assertEqual([], Solution().preorderTraversal(
            None
        ))

        self.assertEqual([1], Solution().preorderTraversal(
            TreeNode(1)
        ))
