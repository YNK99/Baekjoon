def solution(n):
    answer = 0
    nums = []
    for i in str(n):
        nums.append(i)
    nums = sorted(nums)[::-1]
    answer = int("".join(nums))
    return answer