def solution(command):
    answer = []
    xy = [0,0]
    bang = [1,0,0,0]
    
    for com in command:
        if com =='G':
            if bang[0]==1:
                xy[1] += +1
            elif bang[1] ==1:
                xy[0] +=1
            elif bang[2] ==1:
                xy[1]-=1
            else:
                xy[0]-=1
        elif com=='B':
            if bang[0]==1:
                xy[1] -= +1
            elif bang[1] ==1:
                xy[0] -=1
            elif bang[2] ==1:
                xy[1]+=1
            else:
                xy[0]+=1
        elif com=='R':
            if bang[0]==1:
                bang[0]=0
                bang[1] =1
            elif bang[1] ==1:
                bang[1] =0
                bang[2]=1
            elif bang[2] ==1:
                bang[2]=0
                bang[3]=1
            else:
                bang[3] = 0
                bang[0] =1
        else:
            if bang[0]==1:
                bang[0]=0
                bang[3] =1
            elif bang[1] ==1:
                bang[1] =0
                bang[0]=1
            elif bang[2] ==1:
                bang[2]=0
                bang[1]=1
            else:
                bang[3] = 0
                bang[2] =1
    return xy
                    
