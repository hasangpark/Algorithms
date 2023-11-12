def solution(n, arr1, arr2):
    answer = []
    #1. 지도 1과 지도 2 만들기
    map1 = []
    map2 = []
    for arr in arr1:
        bin_num = bin(arr)[2:]
        if len(bin_num)<n:
            map1.append('0'*(n-len(bin_num))+bin_num)
        else:
            map1.append(bin_num)
    #2. 이진수로 만든거 iterate하면서 값이 1보다크면 # 아니면 ' ' 추가해서 answer에 append
    for arr in arr2:
        bin_num = bin(arr)[2:]
        if len(bin_num)<n:
            map2.append('0'*(n-len(bin_num))+bin_num)
        else:
            map2.append(bin_num)
            
    for i,j in zip(map1,map2):
        ans =''
        for k in range(n):
            if int(i[k]) + int(j[k])>=1:
                ans+= '#'
            else:
                ans+= ' '
        answer.append(ans)
    return answer
