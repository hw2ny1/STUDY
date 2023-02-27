#알파벳
def alph(x):
    A = "ABCDEFGH"
    return A[x]

#DFS 정의
def DFS_1(arr, v, visited):
    # 현재 노드 방문
    visited[v] = True
    # 현재 방문한 노드 출력
    print(v, ' ')
    # 현재 노드와 연결된 다른노드를 재귀적으로 방문
    for i in arr[v]:
        # 연결된 노드의 Visted가 False면 방문
        if not visited[i]:
            DFS_1(arr, i, visited)

#DFS 응용
def DFS_2(arr, v, visited):
    # 현재 노드 방문
    visited[v] = True
    # 현재 방문한 노드 출력
    print(alph(v), end = ' ')
    # 현재 노드와 연결된 다른노드를 재귀적으로 방문
    for i in range(8):
        if arr[v][i] == 1:
            DFS_2(arr, i, visited)

visited = [False for _ in range(8)]
level = 0
arr = [[0,1,1,0,0,0,0,1],
       [0,0,0,0,0,0,0,0],
       [0,0,0,1,1,0,1,0],
       [0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]

node = str(input())
DFS_2(arr,0,visited)