def addDigits(num: int) -> int:
    while num > 0:
        rem = num % 10 + num // 10
        num = rem
        if len(str(num)) == 1:
            break
    return num


addDigits("382")
