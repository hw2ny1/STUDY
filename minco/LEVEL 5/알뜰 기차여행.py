inf = 1e8
N,M = map(int,input().split())
visited = [False] * N

# 가장 저렴한 노선의 인덱스를 반환하는 함수
def getsmallindex(graph):
    cheep = inf
    smallindex = 0
    for i in range(len(graph)):
        if cheep > graph[i] and not visited[i]:
            cheep = graph[i]
            smallindex = i
    return smallindex

def dijkstra(start_node,graph,N,min_distance):
    visited[start_node] = True
    # 결과를 반영할 리스트에 시작노드에서 경로 값을 저장
    for i in range(N):
        min_distance[i] = graph[start_node][i]
        min_distance[start_node] = inf
    # 방문하지 않았고 시작노드와 최단거리인 노드
    
    for nodes in graph:
        min_node = getsmallindex(nodes)
        visited[min_node] = True
        # 해당 노드의 인접한 노드들 간의 거리 계산
        for i in range(N):
            if min_distance[min_node] + graph[min_node][i] < min_distance[i]:
                min_distance[i] = min_distance[min_node] + graph[min_node][i]
    return min_distance

graph = [[inf for _ in range(N)] for _ in range(N)]
min_distance = [inf for _ in range(N)]

for _ in range(M):
    x,y,v = map(int,input().split())
    graph[x][y] = v
min_distance = dijkstra(0,graph,N,min_distance)
if min_distance[N-1] > 100000:
    print('impossible')
else:
    print(min_distance[N-1])