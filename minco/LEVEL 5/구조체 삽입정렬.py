n = int(input())
structure = list()
for i in range(n):
    structure.append(tuple(map(str,input().split())))
structure.sort(key=lambda x: (x[0],x[1]))

for i in range(n):
    print(structure[i][0],structure[i][1])