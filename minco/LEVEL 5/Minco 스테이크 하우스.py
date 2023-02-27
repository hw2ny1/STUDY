N,K = map(int,input().split())

meat = [str(i) for i in range(K+1)]
grade = [str(i) for i in range(K+1)]

find_list = []

def union(a,b):
    if a not in meat:
        a,b = b,a
        union(a,b)
    elif b not in meat:
        a = int(a)
        if grade[a] not in meat:
            for i in grade:
                if i == str(a):
                    grade[i] = b
        else:
            grade[a] = b
    else:
        find_list.append((int(a),int(b)))

for _ in range(N):
    a,b = input().split()
    union(a,b)

for x,y in find_list:
    if grade[x] not in meat:
        grade[y] = grade[x]
    else:
        grade[x] = grade[y]

while grade.count('0') != 0:
    grade.remove('0')

for i in grade:
    print(i,end='')