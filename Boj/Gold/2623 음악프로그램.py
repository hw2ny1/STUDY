import sys
from collections import deque
input = sys.stdin.readline
pd = []
N = 0

N, M = map(int,input().split())

for _ in range(M):
    temp = list(map(int,input().split()))
    pd.append(temp[1:])

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for p in pd:
    for i in range(len(p)-1):
        graph[p[i]].append(p[i+1])
        indegree[p[i+1]] += 1


def topology_sort():
    q = deque()
    for i in range(N, 0, -1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    if len(result) == N:
        print(*result)
    else:
        print(0)


topology_sort()