import sys
input = sys.stdin.readline
inf = 10000000

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [[inf for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    dist[i][i] = 0

for i in range(M):
    a, b = map(int,input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])

x,y,ans = 0,0,1000000
for i in range(1,N+1):
    for j in range(i+1,N+1):
        temp = 0
        for k in range(1,N+1):
            temp += min(dist[k][i],dist[k][j])*2
        if temp < ans:
            x = i;y = j;ans = temp

print(x,y,ans)