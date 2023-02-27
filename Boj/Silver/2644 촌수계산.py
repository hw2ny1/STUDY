n = int(input())
A,B = map(int,input().split())
T = int(input())

def DFS(graph,start_node,end_node,cnt):
    global result
    # 현재 방문한 노드를 방문처리하고 출력
    visited[start_node] = True
    if start_node == end_node:
        result = cnt

    # 방문한 노드에서 연결된 노드로 다시 DFS함수 사용
    for i in range(n+1):
        if graph[start_node][i] == 1 and not visited[i]:
            DFS(graph,i,end_node,cnt+1)


graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(T):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False] * (n+1)
result ,cnt = 0, 0

DFS(graph,A,B,cnt)

if result == 0:
    print(-1)
else:
    print(result)