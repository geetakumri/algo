from curses.ascii import SO
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        p1 = 0
        p2 = len(nums) - 1
        res = [0] * len(nums)
        i = len(nums) - 1

        while p1 <= p2:
            if abs(nums[p1]) < abs(nums[p2]):
                res[i] = nums[p2] * nums[p2]
                p2 -= 1

            else:
                res[i] = nums[p1] * nums[p1]
                p1 += 1
            i -= 1

        return res


obj = Solution()
print(obj.sortedSquares([-3, -2, 4, 6, 8, 11]))
