import sys
input = sys.stdin.readline
inf = int(1e8)

N, M, P = map(int,input().split())

graph = [[inf for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
max_g = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
        if graph[i][j] != inf and graph[i][j] > max_g:
            max_g = graph[i][j]

print(max_g)