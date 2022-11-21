from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
visited = [0] * (N+1)
graph = [[] for c in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[end] += [start]
    graph[start] += [end]

graph = [sorted(c, reverse = True) for c in graph]    # 내림차순!
cnt = 1

def bfs(visited, graph, R):
    global cnt
    que = deque([R])
    visited[R] = cnt
    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                que.append(i)
                cnt += 1
                visited[i] = cnt

bfs(visited, graph, R)

print(*visited[1:], sep = '\n')