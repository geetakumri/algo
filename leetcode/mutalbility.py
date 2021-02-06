# dictionaries are mutable. u only cretae new object ,you cant modify them

# integes are immutable , so as float ,strings and tuples -
my_int = 5
print(id(my_int))

my_int += 1  # my_int.__add__(self, 1) = selv.value +=1
print(id(my_int))

friends = ['rofl', 'jose']
print(id(friends))
friends.append('joe')
print(id(friends))

# is is used to compare ids
# add_balance(*t) - unpacking same as add_balance(t[0],t[1])
# obj =[User(**data) for data in users] -> dictionary unpacking

