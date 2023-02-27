import sys
from collections import deque
input = sys.stdin.readline

box = []
cnt = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

M,N = map(int,input().split())
for _ in range(N):
    box.append(list(map(int,input().split())))

def BFS():
    q = deque([])
    z = 0
    for x in range(N):
        for y in range(M):
            if box[x][y] == 1:
                q.append((x,y,z))
    while q:
        x,y,z = q.popleft()
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M and box[x+dx[i]][y+dy[i]] == 0:
                box[x+dx[i]][y+dy[i]] = 1
                q.append((x+dx[i],y+dy[i],z+1))
    return z

cnt = BFS()
temp = 0
for x in range(N):
    for y in range(M):
        if box[x][y] == 0:
            temp = -1
if temp != -1:
    print(cnt)
else:
    print(-1)