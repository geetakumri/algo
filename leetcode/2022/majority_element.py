from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr, count = (
            nums[0],
            1,
        )  # curr will store the current majority element, count will store the count of the majority
        for i in range(1, len(nums)):
            count += (
                1 if curr == nums[i] else -1
            )  # if i is equal to current majority, they're in same team, hence added, else one current majority and i both will be dead
            if not count:  # if count is 0 means King is de-throwned
                curr = (
                    nums[i + 1] if i + 1 < len(nums) else None
                )  # the next element is the new King
                count = 0  # starting it with 0 because we can't increment the i of the for loop, the count will be 1 in next iteration, and again the battle continues after next iteration
        return curr


obj = Solution()
print(obj.majorityElement([1, 2, 1, 3, 1]))
