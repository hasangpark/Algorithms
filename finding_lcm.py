from math import gcd
def solution(arr):
    arr = sorted(arr)
    answer = arr[0]
    
    for a in arr:
        answer = answer*a // gcd(answer,a)
        
    return answer
