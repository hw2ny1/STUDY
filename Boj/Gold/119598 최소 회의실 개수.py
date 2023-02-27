import heapq
import sys

N = int(input())
input = sys.stdin.readline
Time = []

for _ in range(N):
    s,t = map(int,input().split())
    Time.append((s,t))

Time.sort(key = lambda x : (x[0],x[1]))
class_list = []
heapq.heappush(class_list,Time[0][1])

for i in range(1,N):
    if Time[i][0] < class_list[0]:
        heapq.heappush(class_list,Time[i][1])
    else:
        heapq.heappop(class_list)
        heapq.heappush(class_list,Time[i][1])

print(len(class_list))