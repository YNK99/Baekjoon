def solution(clothes):
    d = {c[1]:[] for c in clothes}
    
    for c in clothes:
        d[c[-1]].append(c[0])
    
    result = 1
    
    for i in d:
        result = result * (len(d[i]) + 1)
    
    return result - 1