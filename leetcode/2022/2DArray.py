class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        lis = []
        a = 0
        for values in d.values():
            while values in lis:
                values -= 1
                a += 1
            if values != 0:
                lis.append(values)
        return a


obj = Solution()
print(obj.minDeletions("aaabbbcc"))
