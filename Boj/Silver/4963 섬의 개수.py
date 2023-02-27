# 방향벡터
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


# 재귀 횟수 안풀어 주면 오류남
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# DFS
def check(x, y):
    bada[x][y] = 0
    for i in range(8):
        cx = x + dx[i]
        cy = y + dy[i]
        # 유망하면 체크
        if 0 <= cx < h and 0 <= cy < w:
            if bada[cx][cy] == 1:
                check(cx, cy)


while True:
    w, h = map(int, input().split())
    # 00 들어올때 까지 반복
    if w == 0 and h == 0:
        break
    bada = []
    total = 0
    for _ in range(h):
        bada.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if bada[i][j] == 1:
                total += 1
                check(i, j)
    print(total)
