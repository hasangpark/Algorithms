import math
def solution(fees, records):
    answer = []
    default_min = fees[0]
    default_fee = fees[1]
    unit_min = fees[2]
    unit_fee = fees[3]
    lasthour = 23
    lastmin = 59
    #re_dict에는 {차량번호:[입출,입출]} 형태로 매핑
    re_dict = {re.split(' ')[1] :[] for re in records}
    for re in records:
        if re.split(' ')[1] in re_dict:
            re_dict[re.split(' ')[1]].append(re.split(' ')[0])

    #time_dict에는 이용시간을 분단위로 매핑함
    time_dict = {re.split(' ')[1]:0 for re in records}
    
    for re in re_dict:
        time = 0
        inout = re_dict[re]
        #inout쌍이 맞을 때
        if len(inout)%2==0:
            for i in range(int(len(inout)/2)):
                intime = inout[2*i]
                outtime = inout[2*i+1]
                # print(intime)
                # print(outtime)
                # print(outtime[:2])
                # print(intime[:2])
                time+=60*(int(outtime[:2])-int(intime[:2])) + int(outtime[3:])-int(intime[3:])
            time_dict[re] += time            
        #inout 쌍이 안 맞을 때   
        else:
            for i in range(int(len(inout)/2)):
                intime = inout[2*i]
                outtime = inout[2*i+1]
                time += 60*(int(outtime[:2])-int(intime[:2])) + int(outtime[3:])-int(intime[3:])
            time+= 23*60 + 59 - int(inout[-1][:2])*60 - int(inout[-1][3:])
            time_dict[re] += time
    answer_dict = {re.split(' ')[1]:0 for re in records}
    for time in time_dict:
        if time_dict[time] <=default_min:
            answer_dict[time] += default_fee
        else:
            answer_dict[time]+=default_fee+math.ceil((time_dict[time]-default_min)/unit_min)*unit_fee
    answer = [x[1] for x in sorted(answer_dict.items(), key= lambda x:x[0])]
    return answer

