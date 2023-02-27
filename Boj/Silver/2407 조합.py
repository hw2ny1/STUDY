n, m = map(int,input().split())
temp = 1
for i in range(n,n-m,-1):
    temp *= i
for i in range(1,m+1):
    temp //= i
print(temp)