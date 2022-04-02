class Solution:
    def __init__(self):
        pass

    def find_nonRepeating_char(self, string1):
        char_count = {}
        for i in string1:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1

        for i in string1:
            if char_count[i] == 1:
                return i


obj = Solution()
print(obj.find_nonRepeating_char("ggreeta"))
