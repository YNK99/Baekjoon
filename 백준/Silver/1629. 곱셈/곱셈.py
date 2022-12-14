import sys
sys.setrecursionlimit(10**6)  # 재귀 횟수 늘리기!

A, B, C = map(int, input().split())

def f(x, c):    # x하고 c 순서주의...ㅠㅠㅠ
    if c == 0:
        return 1
    y = f(x, c//2) % C
    if c % 2 == 0:
        return y*y
    else:
        return y*y*x

print(f(A, B) % C)