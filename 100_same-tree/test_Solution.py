from unittest import TestCase

from Solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_is_same_tree(self):
        # self.assertEqual(True, Solution().isSameTree(
        #     TreeNode(1, TreeNode(2), TreeNode(3)),
        #     TreeNode(1, TreeNode(2), TreeNode(3))
        # ))

        self.assertEqual(False, Solution().isSameTree(
            TreeNode(1, TreeNode(2)),
            TreeNode(1, None, TreeNode(2))
        ))
