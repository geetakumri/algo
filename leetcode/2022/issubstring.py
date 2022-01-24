def is_substring(string, substr):
    k, j = 0, 0

    while j < len(string) and k < len(substr):
        if string[j] == substr[k]:
            k += 1
            j += 1
        elif k != 0:
            k = 0
        else:
            j += 1

    if k == len(substr):
        return True
    else:
        return False


print(is_substring("geeta", "ae"))
