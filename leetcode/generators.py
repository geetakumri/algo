# normal function
def hundred_number():
    nums = []
    i = 0
    while i < 100:
        nums.append(i)
        i += 1
    return nums


print(hundred_number())

print([x * 2 for x in hundred_number()])


# generators
def hundred_number1():
    nums = []
    i = 0
    while i < 100:
        yield i
        i += 1


# print(hundred_number1()) -> print generator function
g = hundred_number1()
print(next(g))
print(next(g))
print(list(g)) # list starts from 2 not from 0 , generators remember where we left

my_range_obj = range(10) # next wont b allowed in range
print(my_range_obj)
print(my_range_obj.__repr__())

#print([x * 2 for x in hundred_number1()])
