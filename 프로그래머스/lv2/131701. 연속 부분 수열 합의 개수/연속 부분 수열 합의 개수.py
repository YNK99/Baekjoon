from collections import deque

def solution(elements):
    
    sums = []
    
    for i in range(1, len(elements) + 1):
        d = deque(maxlen = i)
        for i in elements * 2:
            d.append(i)
            sums.append(sum(d))
        
    return len(set(sums))