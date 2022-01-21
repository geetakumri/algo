'''
2.If you have a list of strings, write a program to return a list where a * is added at the end of each string.
   addstar["a","hello","hai","*"]) --->["a*","hello*","hai*","**"]

'''


def addstar(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i + '*')
    print(new_lst)


if __name__ == "__main__":
    addstar(["a", "hello", "hai", "*"])
