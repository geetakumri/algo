'''
1.If you are a list of integers (that are non negative) write a program to return an integer list of the
   rightmost digits.
   right([1,22,94])   ->[1,2,4]
   right([10,0])      ->[0,0]

'''


def right(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i % 10)
    print(new_lst)


if __name__ == "__main__":
    right([1, 22, 94])
    right([10, 0])
