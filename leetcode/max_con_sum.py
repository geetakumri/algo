from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        add = 0
        result = nums[0]
        for i in nums:
            add += i
            if add > result:
                result = add
            if add < 0:
                add = 0
        return result

res = Solution()
print(res.maxSubArray([-4,-1,-9]))


