def capital(s: str) -> str:
    l = s.split(" ")
    for i in range(len(l)):
        l[i] = l[i].capitalize()

    return " ".join(l)


print(capital("this example is nice"))
