# print 1st and last character of a number
num1 = int(input('enter a number'))
num = str(num1)
print(num[0] + num[-1])
r = num1 % 10
while num1 // 10 != 0:
    num1 = num1 // 10
print(f'{num1}{r}')
