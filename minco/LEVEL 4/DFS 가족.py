arr = [[0,1,1,0,0,0,0,1],
       [0,0,0,0,0,0,0,0],
       [0,0,0,1,1,0,1,0],
       [0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]

string = str(input())
alph = "ABCDEFGH"
string = alph.find(string)
print(string)
position = 0

for i in range(8):
    if arr[i][string] == 1:
        position = i
print(position)
for i in range(8):
    if arr[position][i] == 1:
        print(alph[i],end=" ")