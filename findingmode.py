def solution(array):
    answer = 0
    arr_dict = {key: 0 for key in list(set(array))}
    
    for arr in array:
        arr_dict[arr]+=1
    
    arr_dict = sorted(arr_dict.items(), key=lambda x:x[1], reverse=True)
    if len(arr_dict)<=1:
        return arr_dict[0][0]
    else:
        if arr_dict[0][1] == arr_dict[1][1]:
            return -1
        else:
            return arr_dict[0][0]
