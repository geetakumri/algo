def single_row_keyboard(s):
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    lst = [i for i in keyboard]
    dic = {}
    for i , val in enumerate(lst):
        dic[val] = i
    #print(dic)
    res = 0
    start = 0
    for i in s:
        res = res+ abs(start -dic[i] )
        #print(dic[i])
        start = dic[i]
        #print(start)

    print(res)



single_row_keyboard("hello")