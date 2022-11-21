import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, R = map(int, input().split())
# E = [[]] * N   이거 안됨. 얕은 복사? 첫번째 리스트에만 요소를 추가하고 싶어도 모든 리스트에 추가됨...
visited = [0] * (N+1)
graph = [[] for c in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[end] += [start]
    graph[start] += [end]

cnt = 1
def dfs(graph, R, visited):
    global cnt
    visited[R] = cnt
    cnt += 1
    for i in sorted(graph[R], reverse = True):
        if visited[i] == 0:
            dfs(graph, i, visited)

dfs(graph, R, visited)
print(*visited[1:], sep = '\n')