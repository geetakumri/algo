from itertools import permutations
import numpy as np
a = ['9','8']
b = np.random.randint(10,size=8)
phone = ('').join(a)
for i in b:
    phone += str(i)
print(phone)

ph_combinations = permutations(range(10), 8)
for i in ph_combinations:
    print(i)


