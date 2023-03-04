import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split())) + [0,0]
total = 0


def get_lamen_1(i,k):
    global total
    total += 3*k


def get_lamen_2(i,k):
    global total
    lst[i] -= k
    lst[i+1] -= k
    total += 5*k


def get_lamen_3(i,k):
    global total
    lst[i] -= k
    lst[i + 1] -= k
    lst[i + 2] -= k
    total += 7*k


for l in range(N):
    if lst[l+2] < lst[l+1]:
        get_lamen_2(l, min(lst[l],lst[l+1]-lst[l+2]))
        get_lamen_3(l, min(lst[l], lst[l + 1], lst[l + 2]))
    else:
        get_lamen_3(l, min(lst[l], lst[l + 1], lst[l + 2]))
        get_lamen_2(l,min(lst[l],lst[l+1]))
    get_lamen_1(l,lst[l])

print(total)