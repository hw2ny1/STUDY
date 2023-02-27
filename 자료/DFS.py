alphabet = ["A", "B", "C", "D", "E", "F"]

adj = []
for _ in range(6):
    adj.append(list(map(int, input().split())))

def dfs(node, path):
    if 1 not in adj[node]:
        print(path)
        return
    for i in range(6):
        if adj[node][i] > 0:
            dfs(i, path+alphabet[i])
dfs(0, "A")
