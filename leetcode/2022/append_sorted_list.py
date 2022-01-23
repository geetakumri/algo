def append_sorted_list(sorted_arr1,sorted_arr2):
    sorted_array = []
    i = 0
    j = 0

    while (i < len(sorted_arr1) and j < len(sorted_arr2)):
        if sorted_arr1[i] == sorted_arr2[j]:
            sorted_array.append(sorted_arr1[i])
            sorted_array.append(sorted_arr2[j])
            i+=1
            j+=1
        elif(sorted_arr1[i] < sorted_arr2[j]):
            sorted_array.append(sorted_arr1[i])
            i+=1
        else:
            sorted_array.append(sorted_arr1[j])
            j+=1

    while(i<len(sorted_arr1)):
        sorted_array.append(sorted_arr1[i])
        i+=1
    while(j<len(sorted_arr2)):
        sorted_array.append(sorted_arr2[j])
        j+=1

    print(sorted_array)
        
            
append_sorted_list([1,1,2,3],[1,2,3,4])           



