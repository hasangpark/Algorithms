def solution(k, tangerine):
    answer = 0 #답
    
    tan_dict = {key:0 for key in list(set(tangerine))} #딕셔너리생성
    # 카운트하기
    for tan in tangerine:
        tan_dict[tan]+=1
    #리스트로 만들고 내림차순으로 정렬
    t_d_l = list(zip(tan_dict.keys(),tan_dict.values()))
    t_d_l = sorted(t_d_l, key=lambda x: x[1], reverse=True)
    
    t_sum = 0
    for t in t_d_l:
        t_sum += t[1]
        answer+=1
        if t_sum>=k:
            return answer
    return answer
