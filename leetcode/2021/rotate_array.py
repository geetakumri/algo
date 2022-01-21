import numpy as np
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        lst = nums[::-1][:k][::-1]
        #print(lst)
        for i in range(k):
            nums.pop()
        #print(nums)

        return list(np.append(lst, [nums]))
        #return lst+[nums]

                
res = Solution()
print(res.rotate([1,2,3,4,5,6,7],3))
        