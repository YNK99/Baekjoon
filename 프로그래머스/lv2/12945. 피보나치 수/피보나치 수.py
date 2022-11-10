def solution(n):
    fibos = [0] * (n + 1)
    fibos[1] = 1
    fibos[2] = 1
    
    for i in range(3, n+1):
        fibos[i] = fibos[i-1] + fibos[i-2]
    
    return fibos[-1] % 1234567