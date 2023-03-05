import sys
input = sys.stdin.readline

N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
his = []

def dfs():
    if len(his) == M:
        print(*his)
        return
    for i in range(N):
        if not his or his[-1] <= lst[i]:
            his.append(lst[i])
            dfs()
            his.pop()

dfs()