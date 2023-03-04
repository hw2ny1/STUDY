import sys
input = sys.stdin.readline

N, B, C = map(int, input().split())
lst = list(map(int,input().split())) + [0,0]
total = 0
t1,t2,t3 = B,(B+C),(B+2*C)


def get_lamen_1(i,k):
    global total
    total += t1*k


def get_lamen_2(i,k):
    global total
    lst[i] -= k
    lst[i+1] -= k
    total += t2*k


def get_lamen_3(i,k):
    global total
    lst[i] -= k
    lst[i + 1] -= k
    lst[i + 2] -= k
    total += t3*k


for l in range(N):
    if B >= C:
        if lst[l+2] < lst[l+1]:
            get_lamen_2(l, min(lst[l],lst[l+1]-lst[l+2]))
            get_lamen_3(l, min(lst[l], lst[l + 1], lst[l + 2]))
        else:
            get_lamen_3(l, min(lst[l], lst[l + 1], lst[l + 2]))
            get_lamen_2(l,min(lst[l],lst[l+1]))
    get_lamen_1(l,lst[l])

print(total)