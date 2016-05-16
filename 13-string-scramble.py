def string_scramble(str1, str2):
    i = 0
    str1_list = []
    str2_list = []
    while i < len(str1):
        str1_list.append(str1[i])
        i = i + 1
    j = 0
    while j < len(str2):
        str2_list.append(str2[j])
        j = j + 1    
    str1_len = len(str1_list)    
    c = 0
    for c in range(0, str1_len):
        my_char = str1_list[0]
        if my_char not in str2_list:
            return False
            break
        else:
            str1_list.remove(my_char)
            str2_list.remove(my_char)
    return True
