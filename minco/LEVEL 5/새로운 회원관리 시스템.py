n = int(input())
name_list = [list(str(input())) for _ in range(n)]

for i in range(len(name_list)):
    temp = len(name_list[i])
    cnt = 0
    for j in range(temp):
        name_list[i][j] = ord(name_list[i][j])
        if name_list[i][j] >= 65 and name_list[i][j] <=90:
            cnt += 1
    if cnt > 1:
        for k in range(temp):
            if name_list[i][k] >= 97:
                name_list[i][k] -= 32
    elif cnt == 0:
        name_list[i][0] -= 32

name_list_result = []

for i in range(len(name_list)):
    temp_2 = ''
    for j in range(len(name_list[i])):
        temp_2 += chr(name_list[i][j])
    name_list_result.append(temp_2)

name_list_result.sort()

for i in range(len(name_list_result)):
    print(name_list_result[i])