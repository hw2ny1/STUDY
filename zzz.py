import sys
input = sys.stdin.readline

def init(left,right,index):
    if left == right:
        tree[index] = index
        return index
    mid = (left+right)//2
    if tree[init(left,mid,index*2)] < tree[init(mid+1,right,index*2+1)]:
        tree[index] = init(left,mid,index*2)
        return tree[index]
    else:
        tree[index] = init(mid+1,right,index*2+1)
        return tree[index]

N = int(input())
arr = [0] + list(map(int,input().split()))
tree = [1e10] * (4*N)
M = int(input())
init(1, N, 1)
print(tree)
for _ in range(M):
    a = list(map(int,input().split()))
    if a[0] == 2:
        print(tree[1])