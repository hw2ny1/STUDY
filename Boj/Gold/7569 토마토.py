import sys
from collections import deque
input = sys.stdin.readline

box = []
cnt = 0

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

M,N,H = map(int,input().split())

for _ in range(H):
    temp = [list(map(int,input().split())) for _ in range(N)]
    box.append(temp)

def BFS():
    q = deque([])
    t = 0
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if box[z][x][y] == 1:
                    q.append([z,x,y,t])
    while q:
        # for bo in box:
        #     print(*bo)
        # print('----------------')
        z,x,y,t = q.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = 1
                q.append((nz,nx,ny,t+1))
    return t

cnt = BFS()
temp = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 0:
                temp = -1
if temp != -1:
    print(cnt)
else:
    print(-1)