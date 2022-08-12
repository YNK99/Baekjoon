def solution(nums):
    sosu = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                N = nums[i] + nums[j] + nums[k]
                for n in range(2, N):
                    if N % n == 0:
                        break
                    else:
                        if n == N - 1:
                            sosu.append(N)
    answer = len(sosu)

    return answer