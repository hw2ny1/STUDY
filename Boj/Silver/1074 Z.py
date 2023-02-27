import sys


def visited(n, r, c):
    global res

    # 찾는 좌표라면 res를 출력하고 종료
    if r == R and c == C:
        print(int(res))
        exit(0)

    # 탐색 증인 배열 중에 찾는 좌표가 없다면 좌표에 크기를 더한다.
    if not (r <= R < r + n and c <= C < c + n):
        res += n * n
        return

    # 1/2/3/4사분면을 재귀적으로 탐색
    visited(n/2, r, c) # 1사분면
    visited(n/2, r, c + n/2) # 2사분면
    visited(n/2, r + n/2, c) # 3사분면
    visited(n/2, r + n/2, c + n/2) # 4사분면


N, R, C = map(int, sys.stdin.readline().split())
res = 0

# 2^n을 0, 0부터 탐색
visited(2 ** N, 0, 0)