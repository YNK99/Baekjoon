def solution(priorities, location):
    cnt = 0
    
    while priorities[location] != 0:
        for i in range(len(priorities)):
            if priorities[i] >= max(priorities):
                priorities[i] = 0
                cnt += 1
                if priorities[location] == 0:
                    break
            else:
                continue
                
    return cnt