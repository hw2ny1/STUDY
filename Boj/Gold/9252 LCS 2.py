import sys
input = sys.stdin.readline

string1 = input().strip()
string2 = input().strip()

lenst1 = len(string1)
lenst2 = len(string2)

dp = [['' for _ in range(lenst1+1)] for _ in range(lenst2+1)]

for i in range(1,lenst2+1):
    for j in range(1,lenst1+1):
        if string1[j-1] == string2[i-1]:
            dp[i][j] = dp[i-1][j-1]+string1[j-1]
        else:
            if len(dp[i][j-1]) > len(dp[i-1][j]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]

print(len(dp[lenst2][lenst1]))
print(dp[lenst2][lenst1])