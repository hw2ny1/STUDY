import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
rever = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
    rever[b].append((a, c))
    indegree[b] += 1
start, end = map(int, input().split())


def topolozy_sort():
    q = deque()
    q.append(start)
    dp = [0 for _ in range(N+1)]
    while q:
        now = q.popleft()
        for i, cost in graph[now]:
            indegree[i] -= 1
            if dp[now] + cost > dp[i]:
                dp[i] = dp[now] + cost
            if indegree[i] == 0:
                q.append(i)

    q.append(end)
    route = set()
    while q:
        now = q.popleft()
        for i, cost in rever[now]:
            if dp[now] - dp[i] == cost and (now,i) not in route:
                q.append(i)
                route.add((now,i))

    print(dp[end])
    print(len(route))


topolozy_sort()