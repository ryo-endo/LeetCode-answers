from unittest import TestCase

from Solution import TreeNode, Solution


class TestSolution(TestCase):
    def test_postorder_traversal(self):
        self.assertEqual([3, 2, 1], Solution().postorderTraversal(
            TreeNode(1,
                     None,
                     TreeNode(2,
                              TreeNode(3),
                              None
                              )
                     )
        ))
