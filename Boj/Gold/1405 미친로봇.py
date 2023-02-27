dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(r, c, visited, total):
    global ans
    if len(visited) == C+1:
        ans += total
        return
    for i in range(4):
        nr = r + dir[i][0]
        nc = c + dir[i][1]
        if (nr, nc) not in visited:
            visited.append((nr, nc))
            dfs(nr, nc, visited, total*p[i])
            visited.pop()

C, E, W, S, N = map(int, input().split())
p = [E*0.01, W*0.01, S*0.01, N*0.01]
ans = 0

dfs(0, 0, [(0, 0)], 1)
print(ans)