def solution(s):
    result = []
    answer = []
    last = []
    s_list = s.split('},')
    for i in s_list:
        i = i.replace('{','')
        i = i.replace('}','')
        result.append(i)
    for i in result:
        a = i.split(',')
        answer.append(i)
    for i in answer:
        last.append(i.split(','))
    last_answer = []
    max_list = []
    for j in last:
        max_list.append(len(j))
    max_len = max(max_list)
    for i in range(1,max_len+1):
        for j in last:
            if len(j) == i:
                last_answer.append(j)
    a = []
    for i in last_answer:
        for j in i:
            if int(j) not in a:
                a.append(int(j))
    return a
            
