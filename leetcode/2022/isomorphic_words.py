class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        dic_s = {}
        dic_t = {}

        for i in range(len(s)):
            if s[i] in dic_s:
                if dic_s[s[i]] != t[i]:
                    return False
            else:
                dic_s[s[i]] = t[i]

            if t[i] in dic_t.keys():
                if dic_t[t[i]] != s[i]:
                    return False
            else:
                dic_t[t[i]] = s[i]
            # dic_s[s[i]] = t[i]
            # dic_t[t[i]] = s[i]
        return True
