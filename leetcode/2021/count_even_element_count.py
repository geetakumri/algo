from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # iterate over each list element and check lenghth of each elemt is divisble by 2
        def num_div(n):
            count = 0
            while (n > 0):
                n = n // 10
                count += 1

            return count

        c = 0
        for i in nums:
            # if len(str(i))%2 ==0:
            # count +=1
            if num_div(i) % 2 == 0:
                c += 1
        return c

res = Solution()
print(res.findNumbers([555,901,482,1771]))