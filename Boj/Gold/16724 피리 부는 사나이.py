import sys
sys.setrecursionlimit(1000000)


def DFS(x,y):
    global safe_zone
    if not visited[x][y]:
        visited[x][y] = True
        if graph[x][y] == 'R':
            DFS(x, y + 1)
        elif graph[x][y] == 'L':
            DFS(x, y - 1)
        elif graph[x][y] == 'U':
            DFS(x - 1, y)
        elif graph[x][y] == 'D':
            DFS(x + 1, y)
    elif not finished[x][y]:
        safe_zone += 1
    finished[x][y] = True


row, com = map(int, sys.stdin.readline().split())
visited = [[False for _ in range(com)] for _ in range(row)]
finished = [[False for _ in range(com)] for _ in range(row)]
graph = []
safe_zone = 0

for _ in range(row):
    graph.append(list(sys.stdin.readline().strip()))

for i in range(row):
    for j in range(com):
        DFS(i, j)

print(safe_zone)
