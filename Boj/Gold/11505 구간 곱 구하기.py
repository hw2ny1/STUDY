
def init(left, right, index):
    if left == right:
        tree[index] = arr[left]
        return tree[index]
    mid = (left + right)//2
    tree[index] = (init(left, mid, index * 2) * init(mid+1, right, index * 2 + 1))%1000000007
    return tree[index]


def query(left, right, index, qleft, qright):
    if right < qleft or qright < left:
        return 1
    if qleft <= left and right <= qright:
        return tree[index]
    mid = (left + right) // 2
    return (query(left, mid, index*2, qleft, qright) * query(mid+1, right, index*2+1, qleft, qright))%1000000007


def updateNode(index, target, value, start, end):
    # 범위를 벗어남
    if target < start or end < target:
        return
    # 리프 노드
    if start == end:
        tree[index] = value
        return
    mid = (start + end)//2
    updateNode(index*2, target, value, start, mid)
    updateNode(index*2+1, target, value, mid+1, end)
    tree[index] = tree[index*2]*tree[index*2+1] % 1000000007


N, M, K = map(int,input().split())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
tree = [0] * (len(arr)*4)
init(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1:
        updateNode(1, b, c, 1, N)
        arr[b] = c
    elif a == 2:
        print(int(query(1, N, 1, b, c))%1000000007)
