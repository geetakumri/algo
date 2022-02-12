from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)

        return [left, right]

    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1

        return i


obj = Solution()
print(obj.searchRange([1, 2, 4, 8, 8, 8], 8))

"""first = -1
last = -1
if not nums:
return [first,last]
try:
first = nums.index(target)
last = len(nums) - nums[::-1].index(target) - 1
return [first,last]
except:
return [first,last]"""
