from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for s in zip(*strs):
            if len(set(s)) != 1: break
            i += 1

        return strs[0][0:i]


res = Solution()
print(res.longestCommonPrefix(["flower","flow","flight"]))


class Solution1:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        # sort the array and then compare the first and last string
        strs.sort()
        str_start = strs[0]
        str_last = strs[-1]
        count = 0
        for i in range(len(str_start)):
            if (str_start[i] != str_last[i]):
                break
            else:
                count += 1
        if count == 0:
            return ""
        else:
            return str_start[:count]