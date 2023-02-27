graph = [[0,0,1,0,1,1],
         [1,0,0,1,0,0],
         [0,0,0,0,1,0],
         [1,0,0,0,0,0],
         [1,0,0,0,0,0],
         [0,0,0,0,0,0]]

def DFS(start_node,end_node,graph,visited):
    visited.append(start_node)
    if start_node != end_node:
        if graph[start_node][end_node]>0:
                print(len(visited))
        else:
            for i in range(6):
                if graph[start_node][i] > 0 and i not in visited:
                    DFS(i,end_node,graph,visited)
                elif 1 not in graph[start_node] and end_node not in visited and i == 5:
                    print(0)
    elif start_node == end_node:
        print(len(visited)-1)


start_node,end_node = map(int,input().split())
visited = []
DFS(start_node-1,end_node-1,graph,visited)