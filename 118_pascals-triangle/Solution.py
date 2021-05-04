from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        prev_row = [1]
        result.append(prev_row)

        for _ in range(numRows - 1):
            row = []

            row.append(prev_row[0])
            for i in range(len(prev_row) - 1):
                row.append(prev_row[i] + prev_row[i + 1])
            row.append(prev_row[-1])

            result.append(row)
            prev_row = row

        return result
