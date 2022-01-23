
def compresschar(givenstr):
    k = 0
    j = 0
    count =0
    output_str = ""
    while(j<len(givenstr)):
        if(givenstr[k]==givenstr[j]):
            j+=1
            count +=1
        else:
            output_str += givenstr[k]+str(count)
            k = j
            count =0
    output_str += givenstr[k]+str(count)
           
    print(output_str)
       
    
compresschar("aabbbaa")
