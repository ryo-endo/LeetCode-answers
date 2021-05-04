from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for numRow in range(1, numRows):
            # 行の先頭は常に1
            row = [1]
            for i in range(numRow - 1):
                row.append(result[-1][i] + result[-1][i + 1])
            # 行の末尾は常に1
            row.append(1)
            result.append(row)

        return result
