import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    lst = list(map(int,input().split()))
    for i in range(1,len(lst)-1,2):
        graph[lst[0]].append((lst[i],lst[i+1]))


def dfs(now):
    for nex, cost in graph[now]:
        if dist[nex] == -1:
            dist[nex] = dist[now] + cost
            dfs(nex)


dist = [-1 for _ in range(N+1)]
dist[1] = 0
dfs(1)

start = dist.index(max(dist))
dist = [-1 for _ in range(N+1)]
dist[start] = 0
dfs(start)

print(max(dist))