s = set (list([2, 3, 4, 5, 6, 7, 8, 9]))
#n = int(input())
print(s)
#s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    choice = input().split()
    if choice[0] == "pop":
        s.pop()
    elif choice[0] == "remove":
        s.remove(int(choice[1]))
    elif choice[0] == "discard":
        s.discard(int(choice[1]))
