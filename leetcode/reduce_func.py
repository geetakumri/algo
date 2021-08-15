from functools import reduce

l = [1, 2, 3, 4, 5]
n = (input("input numbers : ").split())
lst = reduce(lambda x, y: int(x) + int(y), n)
print(lst)

# print even numbers
lst1 = list(filter(lambda x: x%2 ==0, l))
print(lst1)

# map ()

lst2 = list(map(lambda x : x**2 ,l))
print(lst2)

