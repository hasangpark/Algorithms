def solution(num, total):
    a = []
    b = []
    for i in range(1,10000):
        a = []
        for j in range(i,i+num):
            a.append(j-5000)
        if sum(a) ==total:
            return a
            
            
            
