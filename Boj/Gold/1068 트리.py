import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
tree = list(map(int,input().split()))
M = int(input())
ans = 0

def dfs(k):
    tree[k] = -2
    for i in range(N):
        if tree[i] == k:
            dfs(i)


dfs(M)
for i in range(N):
    if tree[i] != -2 and i not in tree:
        ans += 1
print(ans)