heap = list(str(input()))
result = []
N = len(heap)

def heapify(heap,node,N):
    # heap : heap으로 만들고자 하는 리스트
    # node : 현재 노드
    # N : 리스트의 길이
    
    # 왼쪽 자식
    chdL = node*2 + 1
    # 오른쪽 자식
    chdR = node*2 + 2
    pare = node

    # 자식노드와 부모노드의 크기를 비교하여 작은수 저장
    if chdL <= N-1 and heap[chdL] > heap[node]:
        pare = chdL
    if chdR <= N-1 and heap[chdR] > heap[node]:
        pare = chdR
    
    # 위치가 바뀌어야 한다면
    if pare != node:
        # 위치변경
        heap[pare], heap[node] = heap[node], heap[pare]
        heapify(heap,pare,N)
        
def heapsort(heap):
    j = 0
    while j != N:
        for _ in range(N-j//2):
            for i in range(N-j):
                heapify(heap,i,N-j)
        heap.append(heap.pop(0))        
        j += 1

heapsort(heap)

for i in range(N):
    print(heap[i],end='')