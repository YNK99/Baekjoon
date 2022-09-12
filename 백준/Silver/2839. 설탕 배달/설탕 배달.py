N = int(input())

answer = -1
M = N // 5
if N == 3 or N == 5:
    print(1)
    answer = 1
else:
    for i in range(M, 0, -1):
        if (N - i * 5) % 3 == 0:
            answer = (i + (N - i * 5) / 3)
            print(round(answer))
            break
    if N % 3 == 0 and answer == -1:
        answer = N / 3
        print(round(answer))
if answer == -1:
    print(-1)