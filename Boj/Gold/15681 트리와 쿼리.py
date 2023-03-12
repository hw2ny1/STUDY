import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [1 for _ in range(N+1)]

def dfs(now):
    if visited[now]:
        return dp[now]
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            dp[now] = dp[now] + dfs(next)
    return dfs(now)

dfs(R)

for _ in range(Q):
    print(dp[int(input())])