 # prime prime by Sieve of Eratosthenes

import math
import time


def GeneratePrimes(num_range):

    # Mark all numbers as prime
    list_numbers = num_range * [True]

    # Cross out 0, 1 as they are not primes
    list_numbers[0] = list_numbers[1] = False

    square_root = int(math.sqrt(num_range))
    count = 0
    for p in range(square_root):
        if list_numbers[p] == True:
            for i in range(p * p, num_range, p):
                # Cross out non primes by marking them false
                list_numbers[i] = False

    print("Primes upto " + str(num_range) + " :")
    for p in range(len(list_numbers)):
        if list_numbers[p] == True:
            count += 1
    return count


start_time = time.time()
print(f" prime number between 0 and 1000000000000 : {GeneratePrimes(100000000)}")

print(f"time for execution is: {time.time() - start_time} ")
