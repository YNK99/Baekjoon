def solution(arr):
    m = min(arr)
    arr.remove(m)
    answer = arr
    if len(arr) == 0:
        answer = [-1]
    return answer