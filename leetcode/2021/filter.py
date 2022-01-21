def starts_with_r(friend):
    return friend.startswith('r')


friends = ['rolf', 'jose', 'randy', 'anna', 'mary']
start_with_r = filter(starts_with_r, friends)

# print(next(start_with_r))
# print(next(start_with_r))
# print(next(start_with_r))

print(list(start_with_r))

# we can use lambda
friends = ['rolf', 'jose', 'randy', 'anna', 'mary']
start_with_r = filter(lambda friend: friend.startswith('r'), friends)

# generator way
another_starts_with_r = (f for f in friends if f.startswith('r'))
print(list(start_with_r))


# another filter function
def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


