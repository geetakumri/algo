#Write a Python Program to check if given array is Monotonic?
class Solution :
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in range(len(A) - 1)))

lst = [4,8,9,6,4]

person = Solution()

print(person.isMonotonic(lst))