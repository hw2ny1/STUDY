import sys
sys.setrecursionlimit(10**6)

def DFS_arrayGR(x,y,color):
    visited1[x][y] = True
    if color == 'R' or color == 'G':
        if x < N-1 and not visited1[x+1][y]:
            if grid[x+1][y] == 'R' or grid[x+1][y] == 'G':
                DFS_arrayGR(x+1,y,color)
        if 0 < x and not visited1[x-1][y]:
            if grid[x-1][y] == 'R' or grid[x-1][y] == 'G':
                DFS_arrayGR(x-1,y,color)
        if y < N-1 and not visited1[x][y+1]:
            if grid[x][y+1] == 'R' or grid[x][y+1] == 'G':
                DFS_arrayGR(x,y+1,color)
        if 0 < y and not visited1[x][y-1]:
            if grid[x][y-1] == 'R' or grid[x][y-1] == 'G':
                DFS_arrayGR(x,y-1,color)
    else:
        if x < N-1 and not visited1[x+1][y]:
            if grid[x+1][y] == color:
                DFS_arrayGR(x+1,y,color)
        if 0 < x and not visited1[x-1][y]:
            if grid[x-1][y] == color:
                DFS_arrayGR(x-1,y,color)
        if y < N-1 and not visited1[x][y+1]:
            if grid[x][y+1] == color:
                DFS_arrayGR(x,y+1,color)
        if 0 < y and not visited1[x][y-1]:
            if grid[x][y-1] == color:
                DFS_arrayGR(x,y-1,color)

def DFS_array(x,y,color):
    visited2[x][y] = True
    if x < N-1 and not visited2[x+1][y]:
        if grid[x+1][y] == color:
            DFS_array(x+1,y,color)
    if 0 < x and not visited2[x-1][y]:
        if grid[x-1][y] == color:
            DFS_array(x-1,y,color)
    if y < N-1 and not visited2[x][y+1]:
        if grid[x][y+1] == color:
            DFS_array(x,y+1,color)
    if 0 < y and not visited2[x][y-1]:
        if grid[x][y-1] == color:
            DFS_array(x,y-1,color)

N = int(input())

grid = [list(str(input())) for _ in range(N)]
visited2 = [[False for _ in range(N)] for _ in range(N)]
cnt_not = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            cnt_not += 1
            DFS_array(i,j,grid[i][j])

visited1 = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            cnt += 1
            DFS_arrayGR(i,j,grid[i][j])
print(cnt_not,cnt)