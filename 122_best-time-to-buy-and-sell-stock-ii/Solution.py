from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        last_price = prices[0]

        for price in prices[1:]:
            if last_price < price:
                total_profit += price - last_price
            last_price = price

        return total_profit
