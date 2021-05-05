from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = None
        max_price = None
        profit = 0

        for price in prices:
            if min_price is None or min_price > price:
                min_price = price
                max_price = None
            elif max_price is None or max_price < price:
                max_price = price
                profit = max(profit, max_price - min_price)

        return profit
