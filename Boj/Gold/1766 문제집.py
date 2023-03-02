import sys
input = sys.stdin.readline
import heapq

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1


def topolozy_sort():
    q = []
    for i in range(1,N+1):
        if indegree[i] == 0:
            heapq.heappush(q,i)

    result = []
    while q:
        now = heapq.heappop(q)
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                heapq.heappush(q,i)

    print(*result)

topolozy_sort()