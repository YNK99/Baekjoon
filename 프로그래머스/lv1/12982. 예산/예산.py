def solution(d, budget):
    d = sorted(d)
    cnt = 0
    
    for i in d:
        budget -= i
        if budget >= 0:
            cnt += 1
    
    return cnt
            