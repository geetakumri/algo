def max_min_time(time_input):
    hh1 = time_input[0]
    hh2 = time_input[1]
    mm1 = time_input[3]
    mm2 = time_input[4]

    if mm2 == '?':
        mm2 = '9'
    if mm1 == '?':
        mm1 = '5'

    if hh2 == '?' and hh1 == '?':
        hh2 = '3'
        hh1 = '2'
    elif hh2 == '?' and hh1 != '?':
        if int(hh1) < 2:
            hh2 = '9'
        elif int(hh1) == 2:
            hh2 = '3'
    if hh1 == '?':
        if int(hh2) < 4:
            hh1 = '2'
        else:
            hh1 = '1'

    str1 = hh1 + hh2 + ":" + mm1 + mm2
    print(str1)


max_min_time('2?:20')
