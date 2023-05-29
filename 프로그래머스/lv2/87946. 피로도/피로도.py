from itertools import permutations

def solution(k, dungeons):
    result = 0
    
    for i in list(permutations(dungeons)):
        cnt = 0
        start = k
        for j in i:
            if j[0] <= start:
                start -= j[1]
                cnt += 1
            else:
                break
        result = max(result, cnt)
        
    return result