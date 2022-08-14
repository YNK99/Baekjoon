def solution(s):
    nums = [str(c) for c in range(0, 10)]
    if len(s) == 4 or len(s) == 6:
        answer = True
    else:
        answer = False
    for i in s:
        print(i)
        if i in nums:
            continue
        else:
            answer = False
            break
    return answer