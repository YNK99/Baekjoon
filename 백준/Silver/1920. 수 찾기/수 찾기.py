N = int(input())
A1 = list(map(int, input().split()))
M = int(input())
A2 = list(map(int, input().split()))

same = set(A1) & set(A2)

for i in A2:
    if i in same:
        print(1)
    else:
        print(0)