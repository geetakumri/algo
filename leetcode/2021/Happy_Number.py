def isHappyNumber(num):
    rem = sum = 0;

    # Calculates the sum of squares of digits
    while (num > 0):
        rem = num % 10;
        sum = sum + (rem * rem);
        num = num // 10;
    return sum;


# num = int(input('Enter a number :' ));


for i in range(1, 101):
    result = i
    while (result != 1 and result != 4):
        result = isHappyNumber(result);
        # Happy number always ends with 1
        if (result == 1):
            print(str(i) + " is a happy number");
        # Unhappy number ends in a cycle of repeating numbers which contain 4
        elif (result == 4):
            print(str(i) + " is not a happy number");