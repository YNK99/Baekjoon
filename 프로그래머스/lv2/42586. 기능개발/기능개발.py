import math

def solution(progresses, speeds):
    day = []
    cnt = []
    
    for i, j in zip(progresses, speeds):
        if day == []:
            day.append(math.ceil((100-i) / j))
        else:
            if max(day) < math.ceil((100-i) / j):
                cnt.append(len(day))
                day = []
                day.append(math.ceil((100-i) / j))
            else:
                day.append(math.ceil((100-i) / j))
        
    if day != []:
        cnt.append(len(day))
    
    return cnt