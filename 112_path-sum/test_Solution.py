from unittest import TestCase

from Solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_has_path_sum(self):
        self.assertEqual(True, Solution().hasPathSum(
            TreeNode(5,
                     TreeNode(4,
                              TreeNode(11,
                                       TreeNode(7),
                                       TreeNode(2)
                                       )
                              ),
                     TreeNode(8,
                              TreeNode(13),
                              TreeNode(4,
                                       TreeNode(1))
                              )
                     ),
            22
        ))

        self.assertEqual(False,Solution().hasPathSum(
            TreeNode(1,
                     TreeNode(2)
                     ),
            1
        ))
