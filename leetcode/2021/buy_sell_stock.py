from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in prices[1:]:
            if buy < i:
                buy = i
            elif(i>buy):
                profit = i  -buy
            elif(profit >max_profit):
                max_profit = profit
res = Solution()
print(res.maxProfit([7,1,5,3,6,4]))