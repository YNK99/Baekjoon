N, T = map(int, input().split())

a = map(int, input().split())

A = list(a)

for i in A:
    if i < T:
        print(i)