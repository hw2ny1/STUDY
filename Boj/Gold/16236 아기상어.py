import sys
from collections import deque
import heapq
input = sys.stdin.readline


dir = [(-1,0),(0,-1),(1,0),(0,1)]


def bfs(str_x,str_y):
    global shark
    q = deque([[str_x,str_y,0]])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[str_x][str_y] = True
    history = []
    while q:
        x,y,cnt = q.popleft()
        if arr[x][y] and arr[x][y] < shark_level:
            heapq.heappush(history,[cnt,x,y])
        for dx,dy in dir:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:continue
            if visited[nx][ny]:continue
            if arr[nx][ny] > shark_level:continue
            q.append((nx,ny,cnt+1))
            visited[nx][ny] = True
    if history:
        cnt,x,y = heapq.heappop(history)
        arr[x][y] = 0
        shark = [x,y]
        return cnt
    return -1


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
fishes = [[] for _ in range(10)]
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            fishes[arr[i][j]].append([i, j])
shark = fishes[9].pop()
arr[shark[0]][shark[1]] = 0
shark_level = 2
shark_exp = 0
total = 0
while True:
    temp = bfs(*shark)
    if temp != -1:
        total += temp
        shark_exp += 1
    else:
        break
    if shark_exp == shark_level:
        shark_level += 1
        shark_exp = 0
print(total)