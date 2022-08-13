def solution(num):
    if num == 1:
        answer = 0
    else:
        for i in range(500):
            if num == 1:  
                answer = i
                break
            else:
                if num % 2 != 0:
                    num = num * 3 + 1
                else:
                    num = num / 2
    if num != 1:
        answer = -1
    return answer