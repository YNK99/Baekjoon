def solution(want, number, discount):
    
    w = []
    
    for i, j in zip(want, number):
        for k in range(j):
            w.append(i)
    w = sorted(w)
    cnt = 0
    for i in range(len(discount)-9):
        ten = discount[i:i+10]
        if sorted(ten) == sorted(w):
            cnt += 1
    return cnt