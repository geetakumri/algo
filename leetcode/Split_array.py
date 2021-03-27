arr = []
size = int(input('Enter the size: '))
for i in range (0, size):
    arr.append(int(input('Enter the array element: ')))


n = 2
new_arr = []

for i in range( n+1,len(arr)):
    new_arr.append(arr[i])
for i in range(0,n+1):
    new_arr.append(arr[i])
print(new_arr)
