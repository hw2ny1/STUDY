binary = [4,4,5,7,8,10,20,22,23,24]

def binary_serch(binary,target):
    end = len(binary)-1
    start = 0
    while start <= end:
        mid = (start+end)//2
        if target == binary[mid]:
            return 'O'
        elif target > binary[mid]:
            start = mid +1
        else:
            end = mid -1
    return 'X'

N = int(input())
print(binary_serch(binary,N))