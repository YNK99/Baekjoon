n = int(input())

cnt = 1
def fib(n):
    global cnt
    if n == 1 or n == 2:
        return 1
    else:
        cnt += 1
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    fibo_list = [0] * n
    fibo_list[0] = 1
    fibo_list[1] = 1
    for i in range(2, n):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    return fibo_list

fib(n)
print(cnt, len(fibonacci(n))-2)