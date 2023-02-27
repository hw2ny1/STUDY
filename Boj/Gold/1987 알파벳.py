import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 유망한지 판단
def promising(x, y):
    if 0 <= x < R and 0 <= y < C:
        if check[ord(board[x][y])] == 0:
            return True
    return False


def backtracking(x, y, cnt):
    global cnt_max
    # 최대값보다 클 경우 갱신
    if cnt_max < cnt:
        cnt_max = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 델타 탐색
        if promising(nx, ny):
            check[ord(board[nx][ny])] = 1
            backtracking(x + dx[i], y + dy[i], cnt+1)
            check[ord(board[nx][ny])] = 0


x, y = 0, 0
R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
check = [0] * 100
check[ord(board[0][0])] = 1
cnt_max = 0

backtracking(x, y, 1)

print(cnt_max)