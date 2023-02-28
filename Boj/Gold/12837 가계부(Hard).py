import sys
input = sys.stdin.readline


# def init(left, right, index):
#     if left == right:
#         tree[index] = arr[left]
#         return tree[index]
#     mid = (left + right)//2
#     tree[index] = init(left, mid, index*2) + init(mid+1, right, index*2+1)


def query(left, right, index, qleft, qright):
    if right < qleft or qright < left:
        return 0
    if qleft <= left and right <= qright:
        return tree[index]
    mid = (left + right)//2
    return query(left, mid, index*2, qleft, qright) + query(mid+1, right, index*2+1, qleft, qright)


def update(left, right, index, diff_index, diff):
    if right < diff_index or diff_index < left:
        return
    if left == right:
        tree[index] += diff
        return
    mid = (left + right)//2
    update(left, mid, index*2, diff_index, diff)
    update(mid+1, right, index*2+1, diff_index, diff)
    tree[index] = tree[index*2] + tree[index*2+1]


N, Q = map(int, input().split())
tree = [0] * (N*4)

for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1,N,1,b,c)
    else:
        print(query(1,N,1,b,c))
