from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for price, next_price in zip(prices, prices[1:]):
            if price < next_price:
                total_profit += next_price - price

        return total_profit
