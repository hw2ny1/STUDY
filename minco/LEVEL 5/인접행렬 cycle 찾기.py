N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited =[]
visit =[]

def BFS(graph,visit):
    global visited
    visit = [0]
    while visit:
        temp = visit.pop()
        for i in range(N):
            if graph[temp][i] == 1 and i not in visited:
                visit.append(i)
        visited.append(temp)

BFS(graph,visit)

if visited.count(max(visited,key=visited.count)) > 1:
    print('cycle 발견')
else:
    print('미발견')