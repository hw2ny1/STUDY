graph = [[0,0,1,1,0,1],
         [0,0,0,1,1,1],
         [0,0,0,0,1,1],
         [0,0,0,0,0,0],
         [1,0,0,0,0,1],
         [0,0,0,0,0,0]]

visited = [False] * 6

def DFS(graph,node,visited):
    visited[node] = True
    print(node,end = ' ')
    for i in range(6):
        if graph[node][i] == 1 and visited[i] == False:
            DFS(graph,i,visited)

N = int(input())

DFS(graph,N,visited)
