import re
def solution(input_string):
    answer = ''
    alone = 0
    alpha_dict = {}
    last_dict = {key:0 for key in input_string}
    for i in input_string:
        if i not in alpha_dict:
            alpha_dict[i]=1
        else:
            alpha_dict[i]+=1
    for a in input_string:
        check = 0
        if alpha_dict[a] >=2:
            indices = [i.start() for i in re.finditer(a, input_string)]
            for i in range(0,len(indices)-1):
                if indices[i+1] -indices[i]>1:
                    check+=1
                    last_dict[a] +=1
    for a in last_dict.keys():
        if last_dict[a]>=1:
            answer+=a
            alone+=1
    if alone==0:
        return 'N'
    else:
        return ''.join(sorted(answer))
