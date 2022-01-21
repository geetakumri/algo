def max_finder(lst, N, result_lst = list()):
    while N > 0:
        max_value = max(lst)
        result_lst.append(max_value)
        lst.remove(max_value)
        N-=1
    return result_lst

list1 = []
size = int(input('Enter the size: '))
print('Enter Elements : ')
for i in range (0, size):
    list1 .append(int(input()))
n = int(input('Enter value or N : '))
print(max_finder(list1, n))