import copy

A = [list(map(int,input().split())) for _ in range(3)]
n = input()
B = [list(map(int,input().split())) for _ in range(3)]

C = [[0 for _ in range(3)] for _ in range(3)]

print(A, id(A)) # 셋다 다른 주소
print(B, id(B))
print(C, id(C))

example = [6, 4, 2]
print(id(example), id(A[0])) # 둘다 [6, 4, 2] 지만 주소가 다름 (새로 생성된 example instance)
print(id(example[0]), id(A[0][0])) # 하지만 배열 내의 값들은 같은 주소를 가지게 됨 (6 이라는 객체)

print("---------------")

s=0
while A!=B:
    s+=1
    for i in range(3):
        for j in range(3):
            C[2-j][i] = A[i][j]
    A = C
    print(A, id(A))
    print(C, id(C))
    print(id(A[0]), id(C[0])) # 배열이 같은 것을 참조하니, 배열 내의 값도 당연히 같은 것을 참조
    print()

    if(s==2):
        break 

print(s)
