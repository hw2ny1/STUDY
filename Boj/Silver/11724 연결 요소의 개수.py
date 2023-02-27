import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

visited = [False]*N

def DFS(now):
    visited[now] = True
    for i in range(N):
        if graph[now][i] and not visited[i]:
            DFS(i)
            
cnt = 0
for i in range(N):
    if not visited[i]:
        cnt += 1
        DFS(i)
print(cnt)