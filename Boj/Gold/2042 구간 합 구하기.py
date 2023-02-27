import sys
input = sys.stdin.readline


def init(left, right, index):
    if left == right:
        tree[index] = arr[left]
        return tree[index]
    mid = (left + right)//2
    tree[index] = init(left,mid,index*2) + init(mid+1,right,index*2+1)
    return tree[index]


def query(left, right, index, qleft, qright):
    if qleft > right or qright < left:
        return 0
    if qleft <= left and right <= qright:
        return tree[index]
    mid = (left + right)//2
    return query(left,mid,index*2,qleft,qright) + query(mid+1,right,index*2+1,qleft,qright)


def update(left, right, index, diff_index, diff):
    if diff_index < left or right < diff_index:
        return
    tree[index] += diff
    if left != right:
        mid = (left + right)//2
        update(left, mid, index*2, diff_index, diff)
        update(mid+1, right, index*2+1, diff_index, diff)


N, M, K = map(int,input().split())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
tree = [0] * (len(arr)*4)
init(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1:
        update(1, N, 1, b, c - arr[b])
        arr[b] = c
    elif a == 2:
        print(query(1, N, 1, b, c))
