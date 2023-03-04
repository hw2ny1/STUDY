import sys
input = sys.stdin.readline

N, K = map(int,input().split())
dict = {}
for i in range(K):
    dict[input().rstrip()] = i
result = sorted(dict.items(),key = lambda x : x[1])
if N > len(result):
    N = len(result)
for i in range(N):
    print(result[i][0])