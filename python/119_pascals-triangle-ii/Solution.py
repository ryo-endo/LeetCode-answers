import math
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def comb(n: int, k: int):
            # nCk = n! / k!*(n-k)!
            return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

        return [comb(rowIndex, i) for i in range(rowIndex + 1)]
