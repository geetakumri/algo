lst = []
size = int(input('Enter the size: '))
print('Enter Elements')
for i in range (0, size):
    lst.append(int(input()))


k = int(input('Enter the postion  : '))
n = len(lst)
result  = n *[None]
for i in range(0 , n):
    if (i>=k) :
        new_pos = i-k
    else:
        new_pos = n-k + i
    result[new_pos] = lst[i]
print(result)
