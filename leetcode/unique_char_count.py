from collections import Counter

def unique_char_count(str1):
    lst = []
    for i in str1 :
        lst.append(i)

    print(Counter(lst))


str1 = "kkmjht"
unique_char_count(str1)
