def print_pattern(n):
    num = 1
    for i in range (0,n+1):
        for j in range (0,i+1):
            print(num , end =" ")
            num = num+1
        print()

    return

n = int(input("enter number : "))
print_pattern(n)


 
