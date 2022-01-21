for i in range(1, 101):
    size = len(str(i))
    num = int(i)
    sum = 0
    original_num = i

    while (i != 0):
        r = i % 10
        sum += r ** size
        size -= 1
        i = i // 10
    if (sum == original_num):
        print('The number {} is Disarian number'.format(original_num))
    else:
        print("The number is {} not  Disarian number".format(original_num))
