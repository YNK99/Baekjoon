import math

def solution(n, k):
    answer = 0
    num = ""
    while n > 0:
        n, mod = divmod(n, k)
        num += str(mod)
    num = num[::-1]
    num = num.split("0")
    num = [int(c) for c in num if c != "1" and c != ""]
    for x in num:
        a = 1
        for i in range(2, int(math.sqrt(x)) + 1):
            if x%i == 0:
                a = 0
                break
        answer += a        
            
    return answer