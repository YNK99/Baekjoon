def solution(n):
    answer = ''
    cnt = 0
    while cnt != n:
        if cnt % 2 == 0:
            answer += "수"
        else:
            answer += "박"
        cnt += 1
    return answer