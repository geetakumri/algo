from numpy import array

n, _m = map(int, input().split())
print("{n} , {m} ", n, _m)
a = array([input().split() for _ in range(n)], int)
print(a.min(axis=1).max())
