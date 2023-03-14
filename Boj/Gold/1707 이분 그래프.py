from collections import deque
from sys import stdin
input = stdin.readline

def bfs(start, graph):
    visited[1] = 1
    q = deque([[start, 1]])

    while q:
        now, flag = q.pop()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 2//flag
                q.append([next, 2//flag])
            elif visited[now]*visited[next] != 2:
                return 1
    return 0


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)
    flag = 0
    for _ in range(E):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, V+1):
        if not visited[i]:
            flag += bfs(i, graph)
    print('NO' if flag else 'YES')

