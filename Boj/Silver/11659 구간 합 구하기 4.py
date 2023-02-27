import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
sum_list = [0 for _ in range(N+1)];sum_list[1] = num_list[1]
for i in range(1, N):
    sum_list[i+1] = sum_list[i] + num_list[i+1]

for _ in range(M):
    x, y = map(int, input().split())
    print(sum_list[y] - sum_list[x-1])
