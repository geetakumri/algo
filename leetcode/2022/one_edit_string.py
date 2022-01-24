def one_edit_string(str1,str2):
    if str1 == str2:
        return True
    if len(str1) > len(str2):
        diff = len(str1)- len(str2)
    else:
        diff = len(str2) - len(str1)
    if(diff >1):
        return False
    count = 0
    for i in str1:
        if not i in str2:
            count+=1
    return False if count>1 else True
    
print(one_edit_string('uu','ku'))