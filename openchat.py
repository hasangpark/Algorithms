def solution(record):
    answer= []
    re_list = list(map(lambda x:x.split(' '),record))
    id_check_list = {re[1]:[] for re in re_list}
    name_dict = {re[1]:[] for re in re_list}
    #각 채팅방 참여자들의 최종이름을 넣을 딕셔너리
    for re in re_list:
        if re[0] =='Enter':
            name_dict[re[1]].append(re[2])
        elif re[0] =='Change':
            name_dict[re[1]].append(re[2])

    for re in re_list:
        if re[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(name_dict[re[1]][-1]))
        elif re[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(name_dict[re[1]][-1]))
            
    return answer
