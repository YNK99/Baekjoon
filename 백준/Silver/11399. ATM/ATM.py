N = int(input())
P = list(map(int, input().split()))
P = sorted(P)
t = []
a = 0

for p in P:
    a += p
    t.append(a)

print(sum(t))
