import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
visited = [0] * (N+1)

for i in range(1, N+1):
    a, b = map(int, input().split())
    graph[i].append(b)
    graph[i].append(a)
    indegree[a] += 1
    indegree[b] += 1

def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] < 2:
            q.append(i)
            visited[i] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] < 2 and not visited[next]:
                visited[next] = 1
                q.append(next)

topology_sort()
rlt = []
for i in range(1, N+1):
    if not visited[i]:
        rlt.append(i)

print(len(rlt))
print(*rlt)
