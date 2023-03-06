import sys
input = sys.stdin.readline
N, K = map(int,input().split())
lst = list(map(int,input().split()))
ans = sum(lst[:K])
temp = sum(lst[:K])
for i in range(K,N):
    temp += lst[i]
    temp -= lst[i-K]
    ans = max(ans, temp)
print(ans)