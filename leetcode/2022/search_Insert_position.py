class Solution:
    def __init__(self):
        pass

    def search_and_insert(self, given_list, target):

        start = 0
        end = len(given_list) - 1

        while start <= end:
            mid = (start + end) // 2

            if given_list[mid] == target:
                return mid

            elif given_list[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return end + 1


obj = Solution()
print(obj.search_and_insert([1, 2, 4, 5, 8], 6))
