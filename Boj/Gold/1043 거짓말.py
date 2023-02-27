import sys
input = sys.stdin.readline


def DFS(now):
    visited[now] = 2
    for par in party_member[now]:
        for i in party_[par]:
            if visited[i] != 2:
                DFS(i)


N, M = map(int, input().split())
real = list(map(int, input().split()))
if real[0]:
    visited = [2] + [0 for i in range(M)]
    party_ = [[] for _ in range(N+1)]
    party_member = [[] for _ in range(M+1)]
    for i in range(1, M+1):
        temp = list(map(int,input().split()))
        party_member[i] = temp[1:]
        for y in temp[1:]:
            party_[y].append(i)

    for i in real[1:]:
        for j in party_[i]:
            DFS(j)
    print(visited.count(0))
else:
    print(M)