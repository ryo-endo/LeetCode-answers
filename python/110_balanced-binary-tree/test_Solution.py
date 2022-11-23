from unittest import TestCase

from Solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_is_balanced(self):
        self.assertEqual(True, Solution().isBalanced(
            TreeNode(3,
                     TreeNode(9),
                     TreeNode(20,
                              TreeNode(15),
                              TreeNode(7)
                              )
                     )
        ))
        self.assertEqual(False, Solution().isBalanced(
            TreeNode(1,
                     TreeNode(2,
                              TreeNode(3,
                                       TreeNode(4),
                                       TreeNode(4)
                                       ),
                              TreeNode(3)
                              ),
                     TreeNode(2))
        ))
        self.assertEqual(False, Solution().isBalanced(
            TreeNode(val=1,
                     left=TreeNode(val=2,
                                   left=TreeNode(val=3,
                                                 left=TreeNode(val=4,
                                                               left=None,
                                                               right=None),
                                                 right=None),
                                   right=None),
                     right=TreeNode(val=2,
                                    left=None,
                                    right=TreeNode(val=3,
                                                   left=None,
                                                   right=TreeNode(val=4,
                                                                  left=None,
                                                                  right=None))))
        ))
