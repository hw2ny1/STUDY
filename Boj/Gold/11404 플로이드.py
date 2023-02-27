import sys
input = sys.stdin.readline
inf = 1e9

N = int(input())
M = int(input())
graph = [[inf for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1],c)

for i in range(N):
    graph[i][i] = 0
    for j in range(N):
        for k in range(N):
            graph[j][k]  = min(graph[j][k],graph[j][i]+graph[i][k])

for i in range(N):
    for j in range(N):
        if graph[i][j] == inf:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()