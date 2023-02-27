# deque 라이브러리 불러오기
from collections import deque

def bfs(graph, node, visited):
    queue = deque([node])
    # 현재 노드 방문처리
    visited.append(node)
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 노드하나 꺼내기
        visite = queue.popleft()
        # 탐색 순서 출력
        print(v, end = ' ')
        # 방문하지 않은 인접노드 모드 큐에 넣기
        for i in graph[v]:
            if 1 not in visited:
                queue.append(i)
                visited.append(i)

graph = [[0,0,1,1,0,1],
         [0,0,0,1,1,1],
         [0,0,0,0,1,1],
         [0,0,0,0,0,0],
         [1,0,0,0,0,1],
         [0,0,0,0,0,0]]


visited = []
bfs(graph,0,visited)