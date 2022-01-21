class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        if not s:
            return True
        stack = []
        for _, char in enumerate(s):
            if char in pairs.values():
                stack.append(char)
            elif char in pairs.keys():
                if not stack or stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()
        return not stack

res = Solution()
res.isValid("(89)+(89)")