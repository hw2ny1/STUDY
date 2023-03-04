import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,1,-1]
row, col, N = map(int,input().split())
pool = [[[] for _ in range(col)] for _ in range(row)]
fishing_king = 0

for _ in range(N):
    a,b,c,d,e = map(int,input().split())
    pool[a-1][b-1].append([c,d-1,e])


def fishing(i):
    for j in range(row):
        if pool[j][i]:
            s,d,z = pool[j][i].pop()
            return z
    return 0


def shark_move():
    shark = deque()
    for i in range(row):
        for j in range(col):
            if pool[i][j]:
                s, d, z = pool[i][j].pop()
                shark.append([i, j, s, d, z])
    while shark:
        r, c, s, d, z = shark.popleft()
        r, c = move(r, c, s, d)
        pool[r][c].append([s, d, z])
        
        
def move(r, c, s, d):
    if d == 0 or d == 1:
        nc = c
        
    elif d == 2 or d == 3:
        nr = r
        
    return nr, nc
    


score = 0
while fishing_king < col:
    score += fishing(fishing_king)
    shark_move()
    fishing_king += 1

print(score)
