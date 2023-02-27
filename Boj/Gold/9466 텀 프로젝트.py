import sys
sys.setrecursionlimit(1000000)


def DFS(node_now):
    global team
    check.append(node_now)
    visited[node_now] = True
    if not visited[union[node_now]]:
        DFS(union[node_now])
    elif not finished[union[node_now]]:
        var = check.index(union[node_now])
        team += check[var:]
    finished[node_now] = True


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    visited = [False for _ in range(N + 1)]
    finished = [False for _ in range(N + 1)]
    union = [0] + list(map(int, sys.stdin.readline().split()))
    team = []
    for i in range(1, N + 1):
        check = []
        DFS(i)

    print(N - len(team))
