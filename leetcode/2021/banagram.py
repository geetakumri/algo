# For a given 2 strings s1 and s2 . If the all the letters are same in both the strings except difference of one letter

def banagram(str1,str2):
    if len(str1) != len(str2):
        return False

    char_and_its_count ={}

    for i in str1:
        if i in char_and_its_count:
            char_and_its_count[i]+=1
        else:
            char_and_its_count[i]=1
    
   
    for i in str2:
        if i in char_and_its_count:
            char_and_its_count[i]-=1
        
    count_ocrr_one = 0
        
    for count in char_and_its_count.values():
        if count < 0 or count > 1:
            return False
        elif count == 1:
            count_ocrr_one += 1
    
    if (count_ocrr_one == 1):
        return True
    return False
    
    
        


print(banagram('geet','geat')) #True
print(banagram('geet','gaat')) #False
print(banagram('geet','geet')) #False
print(banagram('get','goei')) #False