from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, nonzero = 0, 0
        while zero < len(nums) and nonzero < len(nums):
            if nums[zero] != 0:
                zero += 1
            else:
                if zero < nonzero and nums[nonzero] != 0:
                    nums[zero], nums[nonzero] = nums[nonzero], nums[zero]
                nonzero += 1
        print(nums)


res = Solution()
res.moveZeroes([0,0,1,2])
