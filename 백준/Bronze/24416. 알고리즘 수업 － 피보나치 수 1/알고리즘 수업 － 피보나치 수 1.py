# 파이썬으로 한 건 틀렸는데 파이파이3로 한 건 맞았습니다ㅠㅠㅠ
# PyPy3가 Python3 실행시 시간이 매우 오래 걸린다는 것을 개선하려고 JIT컴파일 방식을 도입해서라고 합니다...!
# 사실... 무슨 소린지 이해 못했습니다.
# 근데 간단한 코드는 파이썬이 더 낫다니까 적절하게 쓰라고 합니다...!

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
# 재귀는 그냥 출력, 동적 프로그래밍은 -2를 빼줌.
# 왜냐면 동적 프로그래밍에서 반복문을 2부터 시작함
print(cnt, len(fibonacci(n))-2)  