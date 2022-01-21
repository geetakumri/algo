def exp(x):
    return {div(i): sum(i) for i in x}


def mult(x):
    return {i: i * i for i in x}


def div(x):
    return x // x


def sum(x):
    return x + x


def sub(x):
    return x - x


nums = [4, 2, 6, 8, 10]
print(exp(nums))

print(mult(nums))
