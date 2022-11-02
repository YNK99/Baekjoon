def solution(arr):
    answer = []
    last = arr[0]
    answer.append(last)
    for i in arr:
        if i != last:
            answer.append(i)
        last = i
    return answer