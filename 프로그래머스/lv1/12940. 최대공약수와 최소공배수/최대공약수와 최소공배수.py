def solution(n, m):
    nums = sorted([n, m])
    answer = []
    A = 1
    B = 1
    n = nums[0]
    m = nums[1]
    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            n = n / i
            m = m / i
            A = A * i
        else:
            continue
    B = n * m * A
    print(A)
    print(B)
    answer.append(A)
    answer.append(B)
#   6 15
# 3 2 5
    return answer