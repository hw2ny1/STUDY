import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    a,b,c = map(int,input().split())
    indegree[b] += 1
    graph[a].append((b,c))


def topology_sort():
    q = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
    result = []
    total = [1] * (N+1)
    while q:
        now = q.popleft()
        result.append(now)
        for next, cost in graph[now]:
            indegree[next] -= 1
            if cost >= 7:
                cost += 1
            total[next] = max(total[now] + cost, total[next])
            if indegree[next] == 0:
                q.append(next)
    return total


result = topology_sort()
print(max(result))