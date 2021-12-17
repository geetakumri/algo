from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
       '''sum = 0
        for a, b in zip(sorted(seats),sorted(students)):
            sum+=abs(a-b)
        return sum(abs(a - b) for a, b in zip(sorted(seats), sorted(students)))'''
       seats_cnt, students_cnt = [0] * (max(seats) + 1), [0] * (max(students) + 1)
       for seat in seats:
           seats_cnt[seat] += 1
        for student in students:
            students_cnt[student] += 1
        ans = 0
        i = j = 1
        while i < len(students_cnt):
            if students_cnt[i]:
                # find the next available seat
                while j < len(seats_cnt) and not seats_cnt[j]:
                    j += 1
                ans += abs(i - j)
                seats_cnt[j] -= 1
                students_cnt[i] -= 1
            else:
                i += 1
        return ans

res = Solution()
print(res.minMovesToSeat([3,1,5],[2,7,4]))