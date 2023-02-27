# 유니온으로 하니까 못하겠는데
# N = int(input())
# node = ['A','B','C','D']
# P = [i for i in range(4)]

# def Union(a,b):
#     if P[node.index(b)] != P[node.index(a)]:
#         P[node.index(b)] = P[node.index(a)]
#     return

# def Find_cycle(P):
#     if P.count(max(P,key=P.count)) > 1:
#         print('발견')
#     else:
#         print('미발견')

# for _ in range(N):
#     a,b = map(str,input().split())
#     Union(a,b)
# print(P)
# Find_cycle(P)

#DFS
def alph(x):
    alphabet = 'ABCDEFGHIJK'
    return alphabet.find(x)

def DFS(graph,start_node,visited,visit):
    visited.append(start_node)
    for i in range(N):
        if graph[start_node][i] == 1:
            visit.append(i)
    while len(visit) != 0:
        DFS(graph,visit.pop(),visited,visit)

M = int(input())
N = 4
graph = [[0 for _ in range(N)] for _ in range(N)]
visit = []
visited = []

for _ in range(M):
    a,b = map(alph,input().split())
    graph[a][b] = 1

DFS(graph,0,visited,visit)
if visited.count(max(visited,key=visited.count)) > 1:
    print('발견')
else:
    print('미발견')