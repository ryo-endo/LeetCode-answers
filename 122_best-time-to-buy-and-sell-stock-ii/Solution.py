from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        for i, start in enumerate(prices):
            for j, end in enumerate(prices[i + 1:]):
                if (sale := end - start) <= 0:
                    continue
                profit = max(profit, sale + self.maxProfit(prices[i + j + 2:]))
                max_profit = max(max_profit, profit)

        return max_profit
