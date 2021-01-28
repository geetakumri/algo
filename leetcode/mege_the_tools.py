def merge_the_tools(string, k):
    start = 0;
    end = k;
    while end <= len(string):
        remove_dups(string[start:end])
        start = end
        end = end + k
    return

def remove_dups(s):
    output = ""
    set1 = set()
    for i in s:
        if i not in set1:
            set1.add(i)
            output += i
    print(output)

    return


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
