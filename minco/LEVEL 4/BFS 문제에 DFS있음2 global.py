graph = [[0,0,1,0,2,0],
         [5,0,3,0,0,0],
         [0,0,0,0,0,7],
         [2,0,0,0,8,0],
         [0,0,9,0,0,0],
         [4,0,0,7,0,0]]

visited = [False] * 6

def DFS(graph,node,visited):
    global weight
    visited[node] = True
    print(node,weight)
    for i in range(6):
        if graph[node][i] > 0 and visited[i] == False:
            weight += graph[node][i]
            DFS(graph,i,visited)

N = int(input())
weight = 0
DFS(graph,N,visited)
