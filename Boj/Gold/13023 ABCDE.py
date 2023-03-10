import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now,depth):
    global flag
    if depth == 5:
        flag = 1
        return
    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            dfs(next, depth+1)
            visited[next] = False

flag = 0
visited = [False]*N
for i in range(N):
    visited[i] = True
    dfs(i,1)
    visited[i] = False
    if flag:
        break

print(flag)