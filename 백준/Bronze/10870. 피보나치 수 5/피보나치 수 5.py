N = int(input())
fibo = [0, 1]

if N == 0:
    print(0)    # 0일 때 예외처리!!
else:
    for i in range(2, N+1):
        fibo.append(fibo[i-2] + fibo[i-1])

    print(fibo[-1])