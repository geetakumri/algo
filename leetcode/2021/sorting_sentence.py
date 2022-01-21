class Solution:
    def sortSentence(self, s: str) -> str:
        str1 = s.split(' ')
        lst = [''] * len(str1)
        #lst = []
        # lst = [[] for k in range(len(str1))]
        for s in str1:
            lst[int(s[-1]) - 1] = s[:-1]

        return (" ").join(lst)


res = Solution()
print(res.sortSentence("lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"))
