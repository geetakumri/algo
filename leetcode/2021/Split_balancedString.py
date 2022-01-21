class Solution(object):
    def balancedStringSplit(self, s):
        if not s:
            return
        stack = []
        counter = 0
        for char in s:
            if stack:
                if stack[-1] == char:
                    stack.append(char)
                elif stack[-1] != char:
                    stack.pop()
                continue
            counter += 1
            stack.append(char)
        return counter


a = Solution()
print(a.balancedStringSplit('RLRRLL'))
