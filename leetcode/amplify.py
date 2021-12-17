def amplify(n):
    return [i*10  if i%4==0 else i for i in range(1,n+1)]

print(amplify(4))
print(amplify(3))
print(amplify(25))