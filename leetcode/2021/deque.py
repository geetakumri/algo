import collections
'''from collections import deque
d = deque()
print(d)
d = deque('heello')
print(d)
print(d[0])
print(d.pop())
d.popleft()
d.extend('56')
d.extend([1,2,3])
print(d.extendleft('hey'))

d.rotate(-1)
d = deque('hello', maxlen=5)
print(d)
d.append(1)
print(d)'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        d=dict.fromkeys(s,0)
        for ss,tt in zip(s,t):
            if tt not in d: break
            d[ss] += 1
            d[tt] -= 1
        else:
            return not any(d.values())
        return False

