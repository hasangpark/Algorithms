# from collections import deque
def solution(n, m, section):
    cnt = 0
    paint = []
    # done = deque()
    for sec in section:
        if len(paint) == 0:
            paint.append(sec+m-1)
            cnt +=1 
        elif len(paint) != 0:
            if sec <= paint[-1]:
                continue
            elif sec > paint[-1]:
                paint.append(sec+m-1)
                cnt +=1 
                
    return cnt
