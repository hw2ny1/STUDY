import sys
input = sys.stdin.readline


def init(left, right, index):
    if left == right:
        tree[index] = arr[left]
        return tree[index]
    mid = (left + right)//2
    tree[index] = min(init(left, mid, index*2), init(mid+1, right, index*2 + 1))
    return tree[index]


def query(left, right, index, qleft, qright):
    if left > qright or qleft > right:
        return sys.maxsize
    if qleft <= left and right <= qright:
        return tree[index]
    mid = (left + right)//2
    return min(query(left, mid, index*2, qleft, qright), query(mid+1, right, index*2+1, qleft, qright))


def update():
    pass


N, M = map(int,input().split())
arr = [0]
tree = [0] * (4 * N)
for _ in range(N):
    arr.append(int(input()))
init(1,N,1)
for _ in range(M):
    a, b = map(int,input().split())
    print(query(1,N,1,a,b))
