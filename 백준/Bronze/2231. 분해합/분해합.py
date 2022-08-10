N = input()
M = []

for i in range(1, int(N) + 1):
    S = int()
    for j in str(i):
        S += int(j)
    if i + S == int(N):
        M.append(i)

if len(M) == 0:
    print(0)
else:
    print(min(M))