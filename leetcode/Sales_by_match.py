#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dict1 = {}
    count = 0
    for i in range(len(ar)):
        dict1[ar[i]] = ar.count(ar[i])
    for c in dict1.values():
        count += c//2
    return count


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(sockMerchant(n, ar))

