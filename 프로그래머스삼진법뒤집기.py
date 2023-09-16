def solution(n):
    num = ''
    while True:
        if n>=3:
            num+=str(n%3)
            n = int(n/3)
        else:
            num+=str(n%3)
            break
    answer = 0
    for i in range(len(num)):
        answer += 3**(len(num)-1-i) * int(num[i])
    return answer
    