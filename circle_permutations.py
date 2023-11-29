def solution(elements):
    sum_list = []
    sum_list.append(sum(elements))
    og_len = len(elements)
    answer = 0
    elements = elements+elements[:-2]
    for i in range(1,og_len):
        for j in range(og_len):
            sum_list.append(sum(elements[j:j+i]))
            
    return len(set(sum_list))

#79114791
# 7 9 1 1 4  =>5
# 79 91 11 14 47 => 5
# 791 911 114 147 479 => 5
# 7911 9114 1147 1479 4791=> 5
# 79114 =>1
