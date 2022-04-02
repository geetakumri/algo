import datetime
from math import sqrt


def is_prime(num):

    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def count_prime_num(strt, end):
    count = 0
    for i in range(strt, end):
        if is_prime(i):
            count += 1
    return count


start_time = datetime.datetime.now()
print(
    f" prime number between 0 and 1000000000000 : {count_prime_num(0, 1000000000000)}"
)
end_time = datetime.datetime.now()
time_diff = end_time - start_time
print(f"time for execution is: {time_diff.total_seconds() * 1000} ms")
