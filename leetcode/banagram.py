def banagram(s1,s2):
    count =0
    for i in s1:
        if i not in s2:
            count+=1
    return False if count>1 else True



print(banagram('geet','gee'))

print(banagram('get','goe'))