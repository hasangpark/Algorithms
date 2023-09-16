def solution(s, n):
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in s:
        if i != ' ':
            if i == i.lower():
                tmp = alpha.index(i)
                if tmp+n>25:
                    rev = tmp+n-26
                    answer += alpha[rev]
                else:
                    answer += alpha[tmp+n]
            elif i != i.lower():
                tmp = alpha.index(i.lower())
                if tmp+n>25:
                    rev = tmp+n-26
                    answer += alpha[rev].upper()
                else:
                    answer += alpha[tmp+n].upper()
        else:
            answer += i
            
    return answer
            