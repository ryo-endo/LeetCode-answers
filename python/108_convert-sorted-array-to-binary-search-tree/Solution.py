# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        middle = len(nums) // 2

        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle + 1:])

        return root
