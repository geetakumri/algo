'''class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        y = []
        for p in s:
            y.append(p[::-1])
        print(' '.join(y))
        print(' '.join([sub[::-1] for sub in s.split(' ')]))


res = Solution()
res.reverseWords("Let's take LeetCode contest")
'''


class Solution:
    # Normal reverse Function to reverse values
    def reverse(self, s, low, high):
        while (low <= high):
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

    def reverseWords(self, s: str) -> str:
        curr = 0  # Marks the beignning of word
        s = list(s)  # converted String to list to avoid error as strings are immutable
        for i in range(len(s) - 1):
            if (s[i] == " "):  # if we encounter a blank space then we need to reverse values from curr to i-1
                self.reverse(s, curr, i - 1)
                curr = i + 1  # update curr to point next word's beignning
        self.reverse(s, curr, len(s) - 1)  # reverse the last word
        print("".join(s))  # join the list to return it as a String


res = Solution()
res.reverseWords("Let's take LeetCode contest")