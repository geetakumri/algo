'''players = [
    {
        'name': 'Rolf',
        'numbers': (13, 22, 3, 6, 9)
    },
    {
        'name': 'John',
        'numbers': (22, 3, 5, 7, 9)
    }
]
print(players[0]['numbers'])
print(players[0]['numbers'][0])'''
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = {}
        for i, v in enumerate(nums):
            if v in mapp and i - mapp[v] <= k:
                return True
            mapp[v] = i
        return False




res = Solution()
print(res.containsNearbyDuplicate([1,2,3,1],3))