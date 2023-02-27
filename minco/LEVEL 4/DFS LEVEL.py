#DFS LEVEL
def DFS(arr, node, visited,level,path):
    # 현재 노드 저장, level up
    visited[node] = True
    level += 1
    # 현재 노드와 연결된 다른노드를 재귀적으로 방문
    if level == 2:
            print(path)
    for i in range(len(arr[node])):
        # 연결된 노드의 Visted가 False면 방문
        if arr[node][i] == 1:
            DFS(arr, i, visited,level,path + " " + str(i))

level = -1

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [False for _ in range(n)]

DFS(arr,0,visited,level,'0')