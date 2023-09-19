def solution(participant, completion):
    hash_dict = {}
    sumhash = 0
    for part in participant:
        hash_dict[hash(part)] = part
        sumhash += hash(part)
        
    for comp in completion:
        sumhash -= hash(comp)
        
    return hash_dict[sumhash]