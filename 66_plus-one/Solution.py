from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = map(str, digits)
        n = int(''.join(s)) + 1
        return list(map(int,str(n)))

