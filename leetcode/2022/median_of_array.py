from typing import List


class Solution:
    def __init__(self):
        pass

    def find_median(self, nums1: List[int], nums2: List[int]):
        i, j = 0, 0
        merged = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                merged.append(nums1[i])
                merged.append(nums2[j])
                i = i + 1
                j += 1
            elif nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        print(merged)
        print("********")
        # print(len(merged))

        n = len(merged)
        if n % 2 == 0:
            return (merged[((n - 1) // 2)] + merged[(n) // 2]) / 2
        else:
            return merged[n // 2]


obj = Solution()
print(obj.find_median([1, 2, 5], [3, 4, 6, 7]))
