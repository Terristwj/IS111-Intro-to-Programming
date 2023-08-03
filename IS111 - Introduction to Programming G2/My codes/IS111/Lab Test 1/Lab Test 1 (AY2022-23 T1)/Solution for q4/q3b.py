orig_str = 'ABCDEFGHIJKLMN'
len_list = [2,5,3,1,2,1]
cnct_list = ['-','$','','123',' ']

def construct_string(orig_str, len_list, cnct_list): 
    result = '' 
    start = 0
    # cnct_list.append('')
    for i in range(len(len_list)): 
        result += orig_str[start : len_list[i]+start]
        if i < len(cnct_list): 
            result += cnct_list[i]
        start += len_list[i]
    return result 

