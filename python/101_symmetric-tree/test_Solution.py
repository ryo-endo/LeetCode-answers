from unittest import TestCase

from Solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_is_symmetric(self):
        self.assertEqual(True, Solution().isSymmetric(
            TreeNode(1,
                     TreeNode(2,
                              TreeNode(3),
                              TreeNode(4)
                              ),
                     TreeNode(2,
                              TreeNode(4),
                              TreeNode(3)
                              )
                     )
        ))

        self.assertEqual(True, Solution().isSymmetric(
            TreeNode(3)
        ))

        self.assertEqual(False, Solution().isSymmetric(
            TreeNode(1,
                     TreeNode(2,
                              TreeNode(3),
                              TreeNode(5)
                              ),
                     TreeNode(2,
                              TreeNode(4),
                              TreeNode(3)
                              )
                     )
        ))
