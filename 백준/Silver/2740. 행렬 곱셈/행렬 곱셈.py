N, M = map(int, input().split())
A = [list(map(int, input().split())) for c in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for c in range(M)]
B = list(zip(*B))    # 이중리스트의 행과 열을 바꿔줌
result = [[] for c in range(N)]

for idx, a in enumerate(A):
    for b in B:
        s = 0
        for i, j in zip(a, b):
            s += i * j
        result[idx].append(s)

for r in result:
    print(*r)