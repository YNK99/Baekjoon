import sys
input = sys.stdin.readline

N = int(input())

num = [0] * 10_0011

for _ in range(N):
    n = int(input())
    num[n] += 1

for i in range(10_001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)