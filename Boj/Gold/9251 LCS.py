cha1 = list(input())
cha2 = list(input())
cha1N = len(cha1)
cha2N = len(cha2)

string = [[0 for _ in range(cha2N+1)] for _ in range(cha1N+1)]

for i in range(1,cha1N+1):
    for j in range(1,cha2N+1):
        if cha1[i-1] == cha2[j-1]:
            string[i][j] = string[i-1][j-1] + 1
        else:
            string[i][j] = max(string[i-1][j],string[i][j-1])
 
print(string[cha1N][cha2N])