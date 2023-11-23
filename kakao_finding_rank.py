from itertools import combinations
from collections import defaultdict
from bisect import bisect_left
def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score)#각 조건에 해당하는 점수들이 들어감
    for value in dic.values():
        value.sort()   

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key] #target_list에는 조건에 부합하는 점수 리스트
            idx = bisect_left(target_list, target_score)#점수리스트에서 타겟점수의 위치 참조
            count = len(target_list) - idx#점수 시작점에서 끝지점까지 빼서 리스트 계산
        answer.append(count)      
    return answer
