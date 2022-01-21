from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # iterate over list and compare adjacent elelemts
        # add 1 till the next elemet become greater than next element
        # increase count in each addition operation

        if len(nums) == 1: return 0
        count = 0
        for i in range(1, len(nums)):
            if not (nums[i] > nums[i - 1]):
                diff = (nums[i - 1] - nums[i]) + 1
                count += diff
                nums[i] = diff + nums[i]

        return count

res = Solution()
print(res.minOperations([1,1,1]))

class Solution:
    def minOperations(self, nums) -> int:
        count=0
        value=0
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                value = (nums[i]+1) -nums[i+1]
                nums[i+1] +=value
                count+=value

        return count
