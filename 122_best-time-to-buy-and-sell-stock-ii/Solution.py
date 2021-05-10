from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        last_price = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < last_price:
                last_price = price
                continue
            profit += price - last_price
            last_price = price
            total_profit += profit
            profit = 0

        return total_profit
