from collections import deque

N, M, V = map(int, input().split())
graph = [[] for c in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    
for _ in range(N+1):
    graph[_].sort()   # 예제가 오름차순으로 주어진다는 보장이 없으니까 꼭 정렬!!!

def bfs(graph, V, visited):
    que = deque([V])
    visited[V] = True
    while len(que) != 0:
        v = que.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if visited[i] == False:
                que.append(i)
                visited[i] = True

def dfs(grahp, start, visited):
    visited[start] = True
    print(start, end = ' ')
    for i in graph[start]:
        if visited[i] == False:
            dfs(grahp, i, visited)

visited = [False] * (N+1)
dfs(graph, V, visited)

print("")   # 안 하면 두 줄이 붙어버림

visited = [False] * (N+1)
bfs(graph, V, visited)    # 여기에 다시 프린트하면 안됨... 함수 안에 프린트가 있어서 맨 마지막에 none이 출력되어버림