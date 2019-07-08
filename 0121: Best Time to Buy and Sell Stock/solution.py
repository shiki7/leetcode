class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = 100000
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            max_profit = max(max_profit, price - lowest_price)
        return max_profit
