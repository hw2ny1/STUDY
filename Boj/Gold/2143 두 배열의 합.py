import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

ans = 0
A_dict = dict()

for i in range(n):
    for j in range(i, n):
        A_dict[sum(A[i:j+1])] += 1
        
for i in range(m):
    for j in range(i, m):
        ans += A_dict[T - sum(B[i:j+1])]

print(ans)