def average(array):
    # your code goes here
    set_arr = set(array)
    avg = sum(set_arr) / len(set_arr)
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
