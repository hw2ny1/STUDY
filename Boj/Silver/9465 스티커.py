import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    N = int(input())
    sticker_1 = list(map(int,input().split()))
    sticker_2 = list(map(int,input().split()))

    result1 = [sticker_1[0]]
    result2 = [sticker_2[0]]

    if N > 1:
        result1.append(sticker_2[0]+sticker_1[1])
        result2.append(sticker_1[0]+sticker_2[1])

    for i in range(2,N):
        result1.append(max(result1[i-2],result2[i-2],result2[i-1])+sticker_1[i])
        result2.append(max(result2[i-2],result1[i-2],result1[i-1])+sticker_2[i])
    print(max(result1[N-1],result2[N-1]))