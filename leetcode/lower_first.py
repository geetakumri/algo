'''
3. If you have a list of strings, write a program to display a list where each input string is converted to
    lower case.
    lower(["Choc"]) --------> choc

'''


def lower_case(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i.lower())
    print(new_lst)


if __name__ == "__main__":
    lower_case(["Choc"])
    lower_case(["Hello", "How", "Are", "YOU"])
