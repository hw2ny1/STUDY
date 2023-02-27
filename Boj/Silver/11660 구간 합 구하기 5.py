import sys
input = sys.stdin.readline
N, M = map(int,input().split())
num_lst = [[0 for _ in range(N+1)]]
for _ in range(N):
    num_lst.append([0]+list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,N+1):
        num_lst[i][j] += (num_lst[i-1][j]+num_lst[i][j-1]-num_lst[i-1][j-1])

for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    print(num_lst[x2][y2]+num_lst[x1-1][y1-1]-num_lst[x2][y1-1]-num_lst[x1-1][y2])
