from collections import deque
def solution(queue1, queue2):
    answer = 0
    limit = len(queue1) *4
    check_sum = sum(queue1)+sum(queue2)
    target = int(check_sum/2)
    if sum(queue1) == sum(queue2):
        return 0 #처음부터 같을 때
    if check_sum%2==1:
        return -1 # 합이 홀수일 때
    q1 = deque(queue1)
    q2 = deque(queue2)
    tot1 = sum(q1)
    tot2 = sum(q2)
    while tot1 != target: #큐의 원소의 값의 합이 서로 다를 때
        if answer ==  limit: #다 돌았는데도 다를 때
            return -1
        if tot1>tot2:
            a = q1.popleft()
            q2.append(a)
            tot1-=a
            tot2+=a
            answer+=1
        elif tot2>tot1:
            a = q2.popleft()
            q1.append(a)
            tot2-=a
            tot1+=a
            answer+=1
            
    return answer
