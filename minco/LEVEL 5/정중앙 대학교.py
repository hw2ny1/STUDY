from sys import stdin

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
        for _ in range(M//2):
            for i in range(M):
                heapify(heap,i,M)
        heap.append(heap.pop(0))
        M -= 1
    return heap

N = int(input())
heap = [500]
for _ in range(N):
    heap += list(map(int, stdin.readline().split()))
    heapsort(heap)
    print(heap[len(heap)//2])