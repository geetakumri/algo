from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """max_profit = 0
        best_price_to_buy = prices[0]
        for price in prices:
            if price < best_price_to_buy:
                best_price_to_buy = price
            elif price > best_price_to_buy:
                profit = price - best_price_to_buy
                if profit > max_profit:
                    max_profit = profit
        return max_profit"""
        l, r = 0, 1  # left=buy, right=sell
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit


obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
