import collections
from collections import defaultdict
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_count = defaultdict(int)
        for num in arr:
            num_count[num] += 1
        lucky_num = -1
        for num, count in num_count.items():
            if num == count:
                lucky_num = max(num, lucky_num)
        return lucky_num

        def findLucky(self, arr: List[int]) -> int:
            count = collections.Counter(arr)
            maxi = -1
            for key, value in count.items():
                if (key == value):
                    maxi = max(maxi, key)
            return maxi

        def findLucky(self, arr: List[int]) -> int:
            return max(i if arr.count(i) == i else -1 for i in arr)

a = Solution()
print(a.findLucky([2, 2, 1, 3]))
