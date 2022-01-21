from random import random

lst = ["geeta","saurav","hello","saurav"]
str = " ".join(lst)
print(str)

tup = tuple(lst)
print(tup)

st = set(lst)
print(st)

count = lst.count("saurav")
print(count)

print([[x,lst.count(x)] for x in set(lst)])

#enumerates
values = ["geet","saurav","geeta"]

for i , val in enumerate(values):
    print(i,val)


#set
items = set()
items.add("1")
items.add("2")
items.add("3")
print(items)

print(random()) # values between 0 to1




globvar = 0
def set_globvar_to_one():
    global globvar # Needed to modify global copy of globvar
    globvar = 1
def print_globvar():
    print(globvar) # No need for global declaration to read value of globvar
set_globvar_to_one()
print_globvar() # Prints 1

names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print(sum)

lst1 = [2,3]
lst2 =[4,5,6]
lst3=[7,8,9]

for i in(lst1,lst2,lst3):
    print(i[0])

num = 101
n = num
sum = 0
while n >0:
    rem = n%10
    sum = sum *10 +rem
    n = n//10
print(sum)
if sum ==num:
    print("plindrome")
else:
    print("not palindrome")

# common letters in 2 words

w1= input("enter first word")
w2 = input("enter 2nd word")

comm_words = list(set(w1)& set(w2))
print(comm_words)

