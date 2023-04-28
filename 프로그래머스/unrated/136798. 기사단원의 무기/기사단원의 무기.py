def solution(number, limit, power):
    counter = []
    
    for i in range(1, number+1):
        cnt = 0
        
        for j in range(1, i+1):
            if j**2 <= i:
                if j*j == i:
                    cnt += 1
                else:
                    if i%j == 0:
                        cnt += 2
            else:
                break
                
        if cnt > limit:
            cnt = power
            
        counter.append(cnt)
        
    return sum(counter)