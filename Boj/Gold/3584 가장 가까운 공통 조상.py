import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(input())
    union = [i for i in range(N+1)]
    for _ in range(N-1):
        A, B = map(int, sys.stdin.readline().split())
        union[B] = A
    N1, N2 = map(int, sys.stdin.readline().split())
    if union[N1] == union[N2]:
        print(union[N1])
        continue
    else:
        while True:
            if union[N1] != N1:
                temp = N1
                N1 = union[N1]
                union[temp] = False
            else:
                union[N1] = False
                break
        while True:
            if union[N2]:
                N2 = union[N2]
            else:
                print(N2)
                break
