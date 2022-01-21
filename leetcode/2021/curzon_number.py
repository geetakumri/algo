import math


def is_curzon(num):
    return True if (1 + math.pow(num, 2)) % (num * 2 + 1) == 0 else False


is_curzon(5)    