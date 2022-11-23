from unittest import TestCase

from Solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_min_depth(self):
        self.assertEqual(2, Solution().minDepth(
            TreeNode(3,
                     TreeNode(9),
                     TreeNode(20,
                              TreeNode(15),
                              TreeNode(7)
                              )
                     )
        ))

        self.assertEqual(5, Solution().minDepth(
            TreeNode(2,
                     None,
                     TreeNode(3,
                              None,
                              TreeNode(4,
                                       None,
                                       TreeNode(5,
                                                None,
                                                TreeNode(6)))
                              )
                     )
        ))
        self.assertEqual(1, Solution().minDepth(
            TreeNode(2)
        ))
