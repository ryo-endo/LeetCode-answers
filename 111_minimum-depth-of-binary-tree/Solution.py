# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def countNode(node: TreeNode):
            if not node:
                return None
            if not node.left and not node.right:
                return 1

            return 1 + min(i for i in [countNode(node.left), countNode(node.right)] if i is not None)

        return countNode(root) or 0
