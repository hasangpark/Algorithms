def solution(dart):
    prize = ['*','#']
    great = ['S','D','T']
    check = ''
    answer = []
    
    ##점수/보너스/옵션순으로 나누기
    if dart[-1] in prize:
        check+=dart[-1]
    for d in dart:
        if d in great:
            answer.append(dart[:dart.index(d)+1])
            dart = dart[dart.index(d)+1:]
    for a in answer:
        for aa in a:
            if aa in prize:
                answer[answer.index(a)-1]+=aa
                answer[answer.index(a)] = answer[answer.index(a)][1:]
    answer[-1] = answer[-1]+check
    
    #직전 점수 계산하기 위한 리스트
    score_check_list = [0]*len(answer)
    for a in range(len(answer)):
        cal_list = []
        score = ''
        for aa in answer[a]:
            if aa.isdigit():
                score+=aa
            else:
                cal_list.append(aa)
        score = int(score)
        if len(cal_list)==1:
            if cal_list[0] =='S':
                score_check_list[a] = (score)
            elif cal_list[0] =='D':
                score_check_list[a] = score*score
            else:
                score_check_list[a] = score*score*score
        else:
            if cal_list[1] =='*':
                if cal_list[0] =='S':
                    score_check_list[a] = score*2
                    score_check_list[a-1] = score_check_list[a-1]*2
                elif cal_list[0] =='D':
                    score_check_list[a] = score*score*2
                    score_check_list[a-1] = score_check_list[a-1]*2
                else:
                    score_check_list[a] = score*score*score*2
                    score_check_list[a-1] = score_check_list[a-1]*2
            else:
                if cal_list[0] =='S':
                    score_check_list[a] = score*(-1)
                elif cal_list[0] =='D':
                    score_check_list[a] = score*score*(-1)
                else:
                    score_check_list[a] = score*score*score*(-1)
                     
    return sum(score_check_list)
        
