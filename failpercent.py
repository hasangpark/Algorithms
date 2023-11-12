def solution(N, stages):
    answer= []
    s_dict = {key:0 for key in range(1,N+1)}
    
    
    for i in range(1,N+1):
        challenge = 0
        fail = 0
        for s in stages:
            if s == i:
                fail+=1
                challenge+=1
            elif s>i:
                challenge +=1
            else: 
                continue
                
        if challenge == 0:
            s_dict[i] = 0
        else:
            s_dict[i] = fail/challenge
    s_dict = sorted(s_dict.items(),key =lambda x:x[1],reverse=True)   
    for key in s_dict:
        answer.append(key[0])
    
    return answer
