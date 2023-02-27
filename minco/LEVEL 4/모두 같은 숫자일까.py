graph = [list(map(int,input().split())) for _ in range(3)]

def determinent(graph,node):
    if node == len(graph)-1:
        print(graph[0])
        return
    if graph[node] != graph[node+1]:
        print('x')
        return
    determinent(graph,node+1)

for i in range(3):
    determinent(graph[i],0)
