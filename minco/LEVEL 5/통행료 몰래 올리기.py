def heapify(heap,node,N):
    left = node*2 + 1
    right = node*2 + 2
    pare = node

    if left < N and heap[left] < heap[pare]:
        pare = left
    if right < N and heap[right] < heap[pare]:
        pare = right
    
    if pare != node:
        heap[pare],heap[node] = heap[node],heap[pare]
        heapify(heap,pare,N)

def heapsort(heap):
    M = len(heap)
    while M:
        for _ in range(1):
            for i in range(M):
                heapify(heap,i,M)
        heap.append(heap.pop(0))
        M -= 1
    return heap

def fee(heap,N):
    for _ in range(N-1):
        heapsort(heap)
        heap.append(heap.pop(0)*2)
    return heap.pop(0)*2

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
heap = []

for i in range(n):
    for j in range(i+1,n):
        if arr[i][j] != -1:
            heap.append(arr[i][j])
print(f'{fee(heap,10)}만원')