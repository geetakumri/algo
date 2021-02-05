def multivitamin(ar1, ar2) -> int:
    lst = []
    if len(ar1) == len(ar2):
        for i in range(len(ar1)):
            lst.append(ar2[i] - ar1[i])
            print(lst)
    sorted_lst = sorted(lst)
    print(sorted_lst)
    return 1


juice = [1, 3, 4]
capacity = [2, 3, 6]

multivitamin(juice, capacity)
