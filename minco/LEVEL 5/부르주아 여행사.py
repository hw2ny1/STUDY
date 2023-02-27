import heapq

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

def alph(x):
    A = 'ABCDEFGHIJKL'
    return A[x]

heap=[]
for i in arr:
    for j in i:
        heapq.heappush(heap,-j)
result=[]
while heap:
    result.append(heap.pop(0))
    heapq.heapify(heap)

for i in range(3):
    temp = -result[i]
    for x in range(N):
        for y in range(N):
            if arr[x][y] == temp:
                print(f'{alph(x)}-{alph(y)} {temp}')