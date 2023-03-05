import sys
input = sys.stdin.readline

N, M = map(int,input().split())
lst = sorted(list(map(int,input().split())))
his = []


def dfs():
    if len(his) == M:
        print(*his)
        return
    temp = -1
    for i in range(N):
        if temp != lst[i]:
            his.append(lst[i])
            temp = lst[i]
            dfs()
            his.pop()


dfs()