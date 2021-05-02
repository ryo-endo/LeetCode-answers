from typing import List


class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     for i, first in enumerate(numbers):
    #         second = target - first
    #
    #         if second in numbers[i + 1:]:
    #             return [i + 1, numbers.index(second, i + 1) + 1]
    #
    #     return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if (j := dic.get(target - num)) is not None:
                return [j + 1, i + 1]
            dic[num] = i
