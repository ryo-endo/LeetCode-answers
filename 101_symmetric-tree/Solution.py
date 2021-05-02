# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSame(n: TreeNode, m: TreeNode):
            if n is None and m is None:
                return True
            if n is None or m is None:
                return False
            return (n.val == m.val) and isSame(n.left, m.right) and isSame(n.right, m.left)

        return isSame(root.left, root.right)
