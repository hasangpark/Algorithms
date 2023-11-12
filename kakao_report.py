def solution(id_list, report, k):
    answer = [0]*len(id_list)
    rec ={key: 0 for key in id_list}
    
    for re in set(report):
        a = re.split(' ')[1]
        rec[a] +=1
    
    for re in set(report):
        g = re.split(' ')[0]
        r = re.split(' ')[1]
        if rec[r]>=k:
            answer[id_list.index(g)] +=1
    return answer
