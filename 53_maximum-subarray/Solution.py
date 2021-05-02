from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        sum_list = []
        for num in nums:
            sum = sum + num
            if sum < 0:
                sum = 0
                continue

            sum_list.append(sum)

        return max(sum_list)