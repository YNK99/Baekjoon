def solution(arr, divisor):
    answer = []
    arr = sorted(arr)
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
        else:
            continue
    if len(answer) == 0:
        answer = [-1]
    return answer