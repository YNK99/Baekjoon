def solution(a, b, n):
    cola = 0
    
    while n >= a:
        cola += (n // a) * b
        n = n - (n // a * a) + (n // a) * b
        
    return cola