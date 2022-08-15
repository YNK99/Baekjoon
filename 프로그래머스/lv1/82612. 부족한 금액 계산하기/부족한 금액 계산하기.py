def solution(price, money, count):
    answer = -1
    need = 0
    for c in range(1, count + 1):
        need += price * c
    print(need, money)
    if need - money < 0:
        answer = 0
    else:
        answer = need - money
    return answer