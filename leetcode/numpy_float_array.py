import numpy as np


def arrays(arr1):
    return np.array(arr1[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
