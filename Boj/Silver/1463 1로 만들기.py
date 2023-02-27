N = int(input())

dp = [0] * 1500000

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4,N+1):
    temp = dp[i-1] + 1
    if i % 2 == 0:
        temp = min(temp,dp[i//2]+1)
    if i % 3 == 0:
        temp = min(temp,dp[i//3]+1)
    dp[i] = temp

print(dp[N])