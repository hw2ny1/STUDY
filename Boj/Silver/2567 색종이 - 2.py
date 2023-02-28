import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def promising(x,y):
    temp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 102 and 0 <= ny < 102:
            if paper[nx][ny] == 'c':
                temp += 1
    return temp


N = int(input())
paper = [[0 for _ in range(102)] for _ in range(102)]
for _ in range(N):
    a,b = map(int,input().split())
    for i in range(a+1,a+11):
        for j in range(b+1,b+11):
                paper[i][j] = 'c'

# for pa in paper:
#     print(pa)

cnt = 0
for i in range(102):
    for j in range(102):
        if paper[i][j] != 0:continue
        cnt += promising(i,j)

print(cnt)