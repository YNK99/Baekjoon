def solution(n):
    
    dp = [1, 2]
    
    for i in range(n - 1):
        dp.append(dp[-2] + dp[-1])
        
    return dp[-2] % 1234567
