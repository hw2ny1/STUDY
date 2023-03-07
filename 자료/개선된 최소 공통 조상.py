# 11_개선된 최소 공통 조상.py
import sys
from math import log
input = sys.stdin.readline # 시간 초과를 피하기 위해 빠른 입력 함수
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정


n = int(input())
LOG = int(pow(2, log(n, 2) + 1))
parent = [[0] * LOG for _ in range(n + 1)] # 부모 노드 정보
depth = [0] * (n + 1) # 각 노드까지의 깊이
visited = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)] # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, d):
    visited[x] = True
    depth[x] = d
    for y in graph[x]:
        if visited[y]: # 인접한 노드가 이미 깊이를 구했다면 넘기기
            continue
        parent[y][0] = x # 한 칸 위에 있는 부모에 대한 정보 (2^0번째 부모에 대한 정보) - 인접한 노드의 2^0번째 부모 노드를 자신(x)으로 정해주기
        dfs(y, d + 1) # 인접한 노드에 대해서 현재까지의 노드 깊이 + 1를 깊이로 대입

# 전체 부모 관계를 설정하는 함수 - 다이나믹 프로그래밍을 이용해서 2의 제곱으로 건너뛸 때의 부모 값 기록
def set_parent():
    dfs(1, 0) # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1] # 2의 제곱으로 건너뛸 때의 부모 값 기록 ( 2^i 번째 조상 노드 저장 - j의 2^i의 조상 = j의 2^(i-1) 조상의 2^(i-1) 조상)

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # b가 더 깊도록 설정
    if depth[a] > depth[b]:
        a, b = b, a
    # 먼저 깊이가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i): # 깊이 차이가 충분히 클 경우, 2의 제곱 꼴 만큼 감소하도록 만든 후 (예: 15일 경우, 8-4-2-1로 4번 만에 15만큼 줄어듦)
            b = parent[b][i] # 더 깊은 쪽이 깊이가 줄어들도록 만들어 줌
    # 부모가 같아지도록
    if a == b:
        return a
    # 부모가 같지 않다면
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))