from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
zido = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
cnt = 2
temp = set()
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs_zido(x,y):
    q = deque([])
    q.append((x, y))
    visited[x][y] = True
    zido[x][y] = cnt

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if zido[nx][ny] == 0:
                    temp.add((nx, ny))
                if zido[nx][ny] == 1:
                    visited[nx][ny] = True
                    zido[nx][ny] = cnt
                    q.append((nx, ny))


def bfs_check(land):
    global ans
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque([])

    for i in range(N):
        for j in range(N):
            if zido[i][j] == land:
                q.append((i,j))
                dist[i][j] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if zido[nx][ny] > 0 and zido[nx][ny] != land:
                    ans = min(ans, dist[x][y])
                    return
                if zido[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] +1
                    q.append((nx,ny))


for i in range(N):
    for j in range(N):
        if zido[i][j] == 1 and not visited[i][j]:
            bfs_zido(i,j)
            cnt += 1

ans = sys.maxsize
for k in range(2,cnt):
    bfs_check(k)
print(ans)