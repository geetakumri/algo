n1 = int(input())
set1 = set(list(map(int, input().split())))
n2 = int(input())
set2 = set(list(map(int, input().split())))

diff1 = set1.difference(set2)
diff2 = set2.difference(set1)
lst = (sorted(diff1.union(diff2)))
for i in lst:
    print(i)







