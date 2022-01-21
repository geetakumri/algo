#Write a Python Program to check if given array is Monotonic?
class Monotonic :
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in range(len(A) - 1)))

lst = []
size = int(input('Enter the size: '))
print('Enter Elements')
for i in range (0, size):
    lst.append(int(input()))

obj = Monotonic()

print(obj.isMonotonic(lst))