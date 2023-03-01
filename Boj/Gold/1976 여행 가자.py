import sys
input = sys.stdin.readline


# 부모노드를 확인하는 함수
def parent_check(x):
    if union[x] != x:
        union[x] = parent_check(union[x])
    return union[x]


# 서로 merge하는 함수
def union_check(x,y):
    x = parent_check(x)
    y = parent_check(y)
    if x < y:
        union[y] = x
    else:
        union[x] = y


# 만약 가리키는 루트노드가 다르면 같은 집합에 속해있지 않음
def tour_check():
    temp = union[tour[0] - 1]
    for i in tour:
        if temp != union[i - 1]:
            print('NO')
            return
    print('YES')
    return


N = int(input().strip())
M = int(input().strip())

graph = [list(map(int,input().split())) for _ in range(N)]
tour = list(map(int,input().split()))

union = [i for i in range(N)]

# 인접행렬을 통해서 간선이 있는 노드끼리 merge
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            union_check(i,j)

tour_check()