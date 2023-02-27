N, M = map(int,input().split())

dp1 = [0 for _ in range(M+1)]
dp2 = [0 for _ in range(M+1)]
n = 0

while N != n:
    if n%2 == 1:
        coin = int(input())
        for m in range(1,M+1):
            if m <= coin:
                if m%coin == 0:
                    dp1[m] = dp2[m] + 1
                else:
                    dp1[m] = dp2[m]
            else:
                dp1[m] = dp2[m] + dp1[m-coin]
    else:
        coin = int(input())
        for m in range(1,M+1):
            if m <= coin:
                if m%coin == 0:
                    dp2[m] = dp1[m] + 1
                else:
                    dp2[m] = dp1[m]
            else:
                dp2[m] = dp1[m] + dp2[m-coin]
    n += 1

if N%2 ==0:
    print(dp1[M])
else:
    print(dp2[M])