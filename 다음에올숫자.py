def solution(c):
    answer = 0
    r=0
    d=0
    if c[1]-c[0] == c[2]-c[1]:
        d = c[1]-c[0]
        return c[-1] +d
    elif c[1]/c[0] == c[2]/c[1]:
        return c[-1]*c[1]/c[0]
    
    return 0
