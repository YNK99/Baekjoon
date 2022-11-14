# nCr = n!/r!(n-r)!
N, K = map(int, input().split())

def factorial(x):
    last = 1
    for i in range(1, x+1):
        last *= i
    return last

result = factorial(N) // (factorial(K) * factorial(N-K))

print(result % 10007)