import sys
input = sys.stdin.readline

N, M = map(int,input().split())
lst = sorted(list(map(int,input().split())))
visited = [False] * N
his = []


def dfs():
    if len(his) == M:
        print(*his)
        return
    temp = -1
    for i in range(N):
        if not visited[i] and temp != lst[i]:
            if not his or his[-1] <= lst[i]:
                his.append(lst[i])
                visited[i] = True
                temp = lst[i]
                dfs()
                his.pop()
                visited[i] = False


dfs()