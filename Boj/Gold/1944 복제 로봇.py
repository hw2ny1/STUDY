
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]
union = [i for i in range(M+3)]
link = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 2
node = [[0],[1],]
for i in range(1,N-1):
    for j in range(1,N-1):
        if maze[i][j] == 'S' or maze[i][j] == 'K':
            maze[i][j] = cnt
            node.append([cnt,i,j])
            cnt += 1


def bfs(sn, en, x, y):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    q = deque()
    q.append((x, y, 0))
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny]:continue
            if maze[nx][ny] == '1':continue
            if maze[nx][ny] == en:
                return cnt+1
            visited[nx][ny] = True
            q.append((nx, ny, cnt + 1))
    return sys.maxsize


for i in range(2,M+3):
    for j in range(i+1,M+3):
        temp = bfs(i, j, node[i][1], node[i][2])
        link.append((temp,i,j))
        link.append((temp,j,i))
link.sort()


def parent_check(x):
    if union[x] != x:
        union[x] = parent_check(union[x])
    return union[x]


def union_check(x,y):
    x = parent_check(x)
    y = parent_check(y)
    if union[x] < union[y]:
        union[y] = x
    else:
        union[x] = y


total = 0
for cost, x, y in link:
    if parent_check(x) != parent_check(y):
        union_check(x,y)
        total += cost

for i in range(len(union)):
    union[i] = parent_check(i)

union = set(union)
if total > 1e8 or len(union) != 3:
    print(-1)
else:
    print(total)