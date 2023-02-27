n = int(input())
string = list()


for i in range(n):
    temp = str(input())
    string.append((len(temp),temp))

string.sort(key= lambda x : (x[0],x[1]))

for i in range(n):
    print(string[i][1])