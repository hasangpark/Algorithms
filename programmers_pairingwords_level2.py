def solution(s):
    q = []
    for i in s:
        if len(q)==0:
            q.append(i)
        else:  
            if i == q[-1]:
                q.pop()
               #처음에 이걸로해서 효율성 만족 못했음 => q = q[:-1]
            else:
                q.append(i)   
                
    return 1 if len(q)==0 else 0