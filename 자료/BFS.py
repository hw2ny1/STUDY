# 리스트 앞에서 pop하기 위한 deque 모듈 사용
from collections import deque
# 그래프 하드코딩
graph = [[0,1,1,0,0,0],
         [1,0,0,1,1,0],
         [1,0,0,0,0,1],
         [0,1,0,0,0,0],
         [0,1,0,0,0,0],
         [0,0,1,0,0,0]]
# deque와 방문 확인을 할 리스트 생성
queue = deque([])
visited = []

def BFS(start_node):
    # 큐에 시작노드 추가
    queue.append(start_node)
    # 큐에 노드가 있으면 반복
    while queue:
        # 현재노드로 큐에서 꺼내와 방문처리
        node = queue.pop()
        visited.append(node)
        # 현재 방문한 노드 print
        print(node,end = " ")
        for i in range(6):
            # 만약 다른노드로 가지가 나있고 방문하지않았으면
            if graph[node][i] == 1 and i not in visited:
                # 큐에 노드 추가
                queue.appendleft(i)

BFS(0) # N=0 입력시 0 1 2 3 4 5