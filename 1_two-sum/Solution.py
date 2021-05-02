from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, first in enumerate(nums):
            second = target - first

            if second in nums[i + 1:]:
                j = nums.index(second, i + 1)
                return [i, j]

        return []
