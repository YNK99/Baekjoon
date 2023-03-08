def solution(t, p):
    nums = []
    
    while len(t) >= len(p):
        if int(t[:len(p)]) <= int(p):
            nums.append(int(t[:len(p)]))
        t = t[1:]
        
    return len(nums)