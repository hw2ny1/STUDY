N, M = map(int,input().split())
inf = 1e6
dp = [[inf for _ in range(M+1)] for _ in range(N+1)]

for n in range(1,N+1):
    coin = int(input())
    for m in range(1,M+1):
        c1 = c2 = c3 = inf
        if m < coin:
            c1 = dp[n-1][m]
        if m%coin == 0:
            c2 = m//coin
        if m > coin:
            c3 = min(dp[n][m-coin]+1,dp[n-1][m])
        dp[n][m] = min(c1,c2,c3)
            
if dp[N][M]>=inf:
    print(-1)
else:
    print(dp[N][M])