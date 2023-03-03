from sys import stdin
input = stdin.readline
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

N = int(input())
K = int(input())
bhx, bhy = 0, 0
btx, bty = 0, 0
bam = 0

board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = 1
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 4

L = int(input())
change = deque()
for _ in range(L):
    a, b = map(str, input().split())
    a = int(a)
    change.append((a, b))

T = 0
baam = deque()
baam.append((0,0))
while True:
    T += 1
    nbhx = bhx + dx[bam]
    nbhy = bhy + dy[bam]
    if nbhx < 0 or nbhx >= N or nbhy < 0 or nbhy >= N:break
    if board[nbhx][nbhy] == 1:break
    if board[nbhx][nbhy] == 0:
        bhx = nbhx
        bhy = nbhy
        board[bhx][bhy] = 1
        baam.append((bhx,bhy))
        btx, bty = baam.popleft()
        board[btx][bty] = 0
    elif board[nbhx][nbhy] == 4:
        bhx = nbhx
        bhy = nbhy
        board[bhx][bhy] = 1
        baam.append((bhx,bhy))
    if change and change[0][0] == T:
        T, temp = change.popleft()
        if temp == 'L':
            bam = (bam - 1) % 4
        elif temp == 'D':
            bam = (bam + 1) % 4
    # print(bhx, bhy, btx, bty)
    # print(T)
    # for bo in board:
    #     print(*bo)
    # print('---------------')

print(T)