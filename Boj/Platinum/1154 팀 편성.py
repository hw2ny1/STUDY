from sys import stdin,setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
while True:
    a, b = map(int,input().split())
    if a == -1 and b == -1:break
    graph[a].append(b)
    graph[b].append(a)

