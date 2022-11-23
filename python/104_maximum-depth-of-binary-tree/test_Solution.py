from unittest import TestCase

from Solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_max_depth(self):
        self.assertEqual(3, Solution().maxDepth(
            TreeNode(3,
                     TreeNode(9),
                     TreeNode(20,
                              TreeNode(15),
                              TreeNode(7)
                              )
                     )
        ))
        self.assertEqual(2, Solution().maxDepth(
            TreeNode(1,
                     None,
                     TreeNode(2)
                     )))
        self.assertEqual(1, Solution().maxDepth(
            TreeNode(3)
        ))
        self.assertEqual(0, Solution().maxDepth(
            None
        ))
