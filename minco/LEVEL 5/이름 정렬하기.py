n = int(input())
name_list=list()

for i in range(n):
    temp = str(input())
    name_list.append((len(temp),temp))

name_list.sort(key = lambda x: (x[0],x[1]))

for i in range(n):
    print(name_list[i][1])
