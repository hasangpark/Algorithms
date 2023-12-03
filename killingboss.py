def solution(bandage, health, attacks):
    answer = 0
    first = health
    dic = {a[0]:a[1] for a in attacks}
    yeon = 0
    time = bandage[0]
    heal = bandage[1]
    more = bandage[2]
    for i in range(attacks[-1][0]):
        if i in dic.keys():
            yeon = 0
            health -= dic[i]
            if health<=0:
                return -1
        else:
            yeon+=1
            if yeon == time:
                health += more
                yeon = 0
                if health>first:
                    health = first
            health +=heal
            if health>first:
                    health = first 
    health -= attacks[-1][1]
    if health<=0:
        return -1
    return health
