'''
4.Consider a list of strings, return a list where each string is replaced by 3 copies of the concatenated
    string
    example: Input ->(["a","bb"]) ------> Output ->(["aaa","bbbbbb"])

'''


def three_times(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i * 3)
    print(new_lst)


if __name__ == "__main__":
    three_times(["a", "bb"])
