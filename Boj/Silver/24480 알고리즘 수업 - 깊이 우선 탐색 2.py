import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def DFS(now):
    global cnt
    visited[now] = cnt
    graph[now].sort(reverse=True)
    for nex in graph[now]:
        if not visited[nex]:
            cnt += 1
            DFS(nex)


N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int,input().split())
    graph[x].append(y);graph[y].append(x)

cnt = 1
DFS(R)
for visit in visited[1:]:
    print(visit)