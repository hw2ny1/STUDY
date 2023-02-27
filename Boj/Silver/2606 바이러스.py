import sys

def DFS(graph, start_node):
    global cnt
    visited[start_node] = True
    cnt+=1
    for i in range(n+1):
        if graph[start_node][i] == 1 and not visited[i]:
            DFS(graph, i)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    x, y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False]*(n+1)
result = 0
cnt = 0

DFS(graph, 1)

print(cnt-1)