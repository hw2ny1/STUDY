from collections import deque
import sys
input = sys.stdin.readline
q = []
N, M = map(int, input().split())
indegree = [1] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    q.append((a,b))
q.sort()
for a,b in q:
    graph[a].append(b)
    indegree[b] = max(indegree[a] + 1, indegree[b])

print(*indegree[1:])