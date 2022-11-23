# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        diff = targetSum - root.val
        is_leaf = not root.left and not root.right
        if diff == 0 and is_leaf:
            return True

        return self.hasPathSum(root.left, diff) or self.hasPathSum(root.right, diff)
