from collections import deque
# 인접행렬
graph = [[0,0,0,0,1,0],
         [1,0,1,0,0,1],
         [1,0,0,1,0,0],
         [1,1,0,0,0,0],
         [0,1,0,1,0,1],
         [0,0,1,1,0,0]]
# 큐
queue = deque([])

def BFS(graph,start_node,queue):
    # 큐에 시작노드 넣기
    queue.append(start_node)
    visited = []
    # 큐에 노드가 있는 동안 반복
    while queue:
        # 큐에서 노드하나 빼기
        node = queue.popleft()
        # 방문처리
        visited.append(node)
        print(node)
        # 방문한 노드에서 방문하지 않은 노드를 큐에 추가
        for i in range(6):
            if graph[node][i]> 0 and i not in visited and i not in queue:
                queue.append(i)

N = int(input())
BFS(graph,N,queue)

