import sys
input = sys.stdin.readline
inf = sys.maxsize

result = inf
V,E = map(int,input().split())
roads = [[inf for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    roads[a][b] = c
    
for i in range(1,V+1):
    for j in range(1,V+1):
        for k in range(1,V+1):
            if roads[i][j] > roads[i][k] + roads[k][j]:
                roads[i][j] = roads[i][k] + roads[k][j]

for i in range(1,V+1):
    for j in range(1,V+1):
        if i!=j:
            temp = roads[i][j] + roads[j][i]
            result = min(result,temp)
if result < inf:
    print(result)
else:
    print(-1)