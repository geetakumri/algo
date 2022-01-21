from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]

        return strs[0]


res = Solution()
print(res.longestCommonPrefix(['cars', 'cae', 'card', 'car']))
