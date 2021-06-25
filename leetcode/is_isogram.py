def is_in_order(word):
    if word == "".join(sorted(word)):
        return True
    else:
        return False
print(is_in_order("abca"))