class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = "abcdefghijklmnopqrstuvwxyz"
        sentence = sentence.lower()
        for i in range(len(s)):
            if s[i] in sentence:
                count = 1
            else:
                count = 0
                break

        return True if count == 1 else False


res = Solution()
print(res.checkIfPangram('The quick brown hkj )fox jumps over he lazy dog,?'))

print(set('Aaa'))
