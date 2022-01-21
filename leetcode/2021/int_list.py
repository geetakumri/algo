def filter_list(lst):
    int_list = []
    for i in lst :
        if isinstance(i, int):
            int_list.append(i)
    return int_list

filter_list([1, 2, 3, "a", "b", 4])