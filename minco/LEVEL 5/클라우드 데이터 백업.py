N = int(input())
data = ''
for _ in range(N):
    data += str(input())

def binary_serch(data,N):
    left = 0
    right = len(data)-1
    while left <= right:
        mid = (left+right)//2
        if data[mid] == '#' and (data[mid+1] == '0' or mid == len(data)-1):
            break
        elif data[mid] == '0':
            right = mid - 1
        else:
            left = mid + 1
    a = mid // N
    b = mid % N
    print(a,b)

binary_serch(data,N)