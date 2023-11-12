from itertools import combinations
def solution(str1, str2):
    answer = 0
    # 1.다중집합 만들기
    one_f = []
    for i in range(len(str1)-1):
        j = ''
        if str1[i].isalpha() is not True or str1[i+1].isalpha() is not True:
            continue
        else:
            j+=str1[i].upper()
            j+=str1[i+1].upper()
        one_f.append(j)
    two_f = []
    for i in range(len(str2)-1):
        j = ''
        if str2[i].isalpha() is not True or str2[i+1].isalpha() is not True:
            continue
        else:
            j+=str2[i].upper()
            j+=str2[i+1].upper()
        two_f.append(j)
    
    #2. 교/합 구하기/ set으로 만들고 겹치는 원소의 각 배열의 최솟값으로 배당
    gyo = 0
    hab = 0 
    #교집합구하기 min
    for o in set(one_f):
        if o in two_f:
            gyo += min(one_f.count(o),two_f.count(o))
    #합집합구하기 max, 얘는 str1, str2 두번 해야됨
    for o in set(one_f):
        if o not in two_f:
            hab += one_f.count(o)
        else:
            hab+=max(one_f.count(o),two_f.count(o))
    for t in set(two_f):
        if t not in set(one_f):
            hab+= two_f.count(t)
    if gyo==0 and hab==0:
        answer = 65536
    else:
        answer = int((gyo/hab)*65536)
    return answer
