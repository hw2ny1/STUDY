import sys
input = sys.stdin.readline
from collections import deque
inf  = sys.maxsize
dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, M = map(int, input().split())
A1x, A1y = map(int,input().split())
A2x, A2y = map(int,input().split())
B1x, B1y = map(int,input().split())
B2x, B2y = map(int,input().split())


def bfs(start_x, start_y, end_x, end_y):
    visited = [[['',0] for _ in range(M + 1)] for _ in range(N + 1)]
    visited[start_x][start_y] = ['',0]

    q = deque()
    q.append((start_x, start_y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N+1 or ny < 0 or ny >= M+1:continue
            if board[nx][ny] == board[end_x][end_y]:
                visited[nx][ny][0] = visited[x][y][0]
                visited[nx][ny][1] = visited[x][y][1] + 1
                return visited[nx][ny]
            if not visited[nx][ny][1] and board[nx][ny] == 0:
                visited[nx][ny][0] = visited[x][y][0] + str(nx)+ ' ' + str(ny)+ ' '
                visited[nx][ny][1] = visited[x][y][1]+1
                q.append((nx,ny))


def bfs_2(start_x, start_y, end_x, end_y):
    q = deque()
    q.append((start_x, start_y, 0))
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N+1 or ny < 0 or ny >= M+1:continue
            if board[nx][ny] == board[end_x][end_y]:
                return cnt+1
            if not board[nx][ny] and board[nx][ny] == 0:
                board[nx][ny] = 3
                q.append((nx,ny,cnt+1))
    return inf


board = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
board[A1x][A1y] = 1
board[A2x][A2y] = 2
board[B1x][B1y] = 3
board[B2x][B2y] = 4
total_A = 0
temp, num = bfs(A1x,A1y,A2x,A2y)
total_A += num
temp = list(map(int,temp.split()))
for i in range(0,len(temp)-1,2):
    board[temp[i]][temp[i+1]] = 6
# for bo in board:
#     print(*bo)
total_A += bfs_2(B1x,B1y,B2x,B2y)
# print('----------------------')
board = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
board[A1x][A1y] = 1
board[A2x][A2y] = 2
board[B1x][B1y] = 3
board[B2x][B2y] = 4
total_B = 0
temp, num = bfs(B1x,B1y,B2x,B2y)
total_B += num
temp = list(map(int,temp.split()))
for i in range(0,len(temp)-1,2):
    board[temp[i]][temp[i+1]] = 6
# for bo in board:
#     print(*bo)
total_B += bfs_2(A1x,A1y,A2x,A2y)

total = min(total_A,total_B)
if total > 23372036854775807:
    print('IMPOSSIBLE')
else:
    print(total)