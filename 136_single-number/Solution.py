from itertools import zip_longest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for a, b in zip_longest(nums[::2], nums[1::2]):
            if a != b:
                return a
