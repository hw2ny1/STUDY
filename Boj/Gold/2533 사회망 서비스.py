import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [[] for _ in range(N+1)]
dp = [[0,0] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(now):
    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            dp[now][1] += min(dp[i])
            dp[now][0] += dp[i][1]
    dp[now][1] += 1

visited[1] = True
dfs(1)
print(min(dp[1][0],dp[1][1]))