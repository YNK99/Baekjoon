def solution(k, m, score):
    score = sorted(score)[::-1]
    box = []
    price = 0
    
    for cnt, i in enumerate(score):
        box.append(i)
        if (cnt + 1) % m == 0:
            price += min(box) * m
            box = []
    
    return price