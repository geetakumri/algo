from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        for i in indices:
            res += s[i]
        print(res)
        print(''.join(str(s[i]) for i in indices))
        result = [None] * len(s)
        for letter_ix in range(len(s)):
            result[indices[letter_ix]] = s[letter_ix]
        print (''.join(result))


s = Solution()
s.restoreString("codeleet",[4,5,6,7,0,2,1,3])