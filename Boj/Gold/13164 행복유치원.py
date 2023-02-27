import sys
input = sys.stdin.readline

N, K = map(int,input().split())
child = list(map(int,input().split()))
key = [0] * len(child)
for i in range(len(child)-1):
    key[i] = child[i+1]-child[i]
key.sort()
for _ in range(K-1):
    key.pop()
print(sum(key))