def solution(n):
    prime = [c for c in range(1, n+1)]
    
    for i in prime:
        if i == 1:
            prime[i-1] = False
        
        else:
            if i != False:
                for k in range(i, n+1, i):
                    if prime[k-1] != i:
                        prime[k-1] = False
            else:
                pass        
            
            
    return len(prime) - prime.count(False)