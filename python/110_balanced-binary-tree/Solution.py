# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def countNode(node: TreeNode):
            if not node:
                return 0
            return 1 + max(countNode(node.left), countNode(node.right))

        return abs(countNode(root.left) - countNode(root.right)) <= 1 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)


