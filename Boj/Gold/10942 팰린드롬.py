import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int,input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):dp[i][i] = 1
for i in range(1,N):
    for j in range(N-i):
        if i == 1 and L[j] == L[j+i]:
            dp[j][j+1] = 1
        elif L[j] == L[j+i] and dp[j+1][j+i-1]:
            dp[j][j+i] = 1
M = int(input())
for _ in range(M):
    x, y = map(int,input().split())
    print(dp[x-1][y-1])
