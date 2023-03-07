import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
arr = [0] + list(map(int,input().split()))
tree = [0] * (N * 4)


def init(left, right, index):
    if left == right:
        tree[index] = left
        return tree[index]
    mid = (left + right)//2
    tree[index*2] = init(left, mid, index*2)
    tree[index*2+1] = init(mid+1, right, index*2+1)
    if arr[tree[index*2]] > arr[tree[index*2+1]]:
        tree[index] = tree[index*2+1]
        return tree[index]
    else:
        tree[index] = tree[index*2]
        return tree[index]


def query(left, right, index, qleft, qright):
    if left < qleft or qright < right:
        return sys.maxsize
    if qleft <= left and right <= qright:
        return tree[index]
    mid = (left + right)//2
    temp1 = query(left, mid, index*2, qleft, qright)
    temp2 = query(mid+1, right, index*2+1, qleft, qright)
    if arr[temp1] > arr[temp2]:
        return temp2
    else:
        return temp1


def update(left, right, index, diff_index, diff):
    if diff_index < left or right < diff_index:
        return
    if left == diff_index and diff_index == right:
        tree[index] = diff_index
        arr[diff_index] = diff
        return tree[index]
    mid = (left + right)//2
    update(left, mid, index*2, diff_index, diff)
    update(mid+1, right, index*2+1, diff_index, diff)
    if arr[tree[index*2]] > arr[tree[index*2+1]]:
        tree[index] = tree[index*2+1]
        return tree[index]
    else:
        tree[index] = tree[index*2]
        return tree[index]


init(1,N,1)
M = int(input())
for _ in range(M):
    a = list(map(int,input().split()))
    if a[0] == 2:
        print(query(1,N,1,1,N))
    else:
        update(1,N,1,a[1],a[2])