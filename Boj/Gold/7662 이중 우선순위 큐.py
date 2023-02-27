import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    heap_max = []
    heap_min = []
    n = int(input())
    visited = [0] * n
    for i in range(n):
        a,b = input().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(heap_min,(b,i))
            heapq.heappush(heap_max,(-b,i))
            visited[i] = 1

        if a == 'D':
                if b == -1:
                    while heap_min and not visited[heap_min[0][1]]:
                        heapq.heappop(heap_min)
                    if heap_min:
                        visited[heapq.heappop(heap_min)[1]] = 0
                if b == 1:
                    while heap_max and not visited[heap_max[0][1]]:
                        heapq.heappop(heap_max)
                    if heap_max:
                        visited[heapq.heappop(heap_max)[1]] = 0
    
    while heap_min and not visited[heap_min[0][1]]:
        heapq.heappop(heap_min)
    while heap_max and not visited[heap_max[0][1]]:
        heapq.heappop(heap_max)
    if heap_max and heap_min:
        mn = heap_min[0][0]
        mx = heap_max[0][0]
        print(-mx,mn)
    else:
        print('EMPTY')