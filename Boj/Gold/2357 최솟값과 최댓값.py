import sys
input = sys.stdin.readline


def init(left, right, index):
    if left == right:
        tree[index][0] = arr[left]
        tree[index][1] = arr[left]
        return tree[index][0], tree[index][1]
    mid = (left + right)//2
    left_child = init(left, mid, index*2)
    right_child = init(mid+1, right, index*2+1)
    tree[index][0] = min(left_child[0], right_child[0])
    tree[index][1] = max(left_child[1], right_child[1])
    return tree[index][0], tree[index][1]


def query(left, right, index, qleft, qright):
    if right < qleft or qright < left:
        return 1e11,0
    if qleft <= left and right <= qright:
        return tree[index]
    mid = (left + right)//2
    left_child = query(left, mid, index * 2, qleft, qright)
    right_child = query(mid+1, right, index * 2 + 1, qleft, qright)
    temp_min = min(left_child[0], right_child[0])
    temp_max = max(left_child[1], right_child[1])
    return temp_min, temp_max


def update(left, right, index, diff_index, diff):
    if diff_index < left or right < diff_index:
        return
    if left == right:
        tree[index] = [diff, diff]
        return
    mid = (left + right)//2
    update(left, mid, index*2, diff_index, diff)
    update(mid+1, right, index*2+1, diff_index, diff)
    tree[index] = [min(tree[index*2][0], tree[index*2+1][0]),max(tree[index*2][1], tree[index*2+1][1])]


N, M = map(int,input().split())
arr = [0]
tree = [[0,0] for _ in range((N*4))]
for _ in range(N):
    arr.append(int(input()))
init(1,N,1)
for _ in range(M):
    a,b = map(int,input().split())
    print(*query(1,N,1,a,b))
