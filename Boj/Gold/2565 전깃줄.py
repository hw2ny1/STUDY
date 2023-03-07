import sys
input = sys.stdin.readline

N = int(input())
line = []
for _ in range(N):
    x,y = map(int,input().split())
    line.append((x,y))
line.sort()
# 가장 긴 증가하는 부분수열 구하기
dp = [1] * N
for i in range(1,N):
    for j in range(i):
        if line[j][1] < line[i][1]:
            dp[i] = max(dp[j]+1,dp[i])
print(N-max(dp))