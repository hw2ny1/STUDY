string = [str(input()) for _ in range(5)]
check = 0
for i in range(5):
    string[i] = string[i][0]+string[i][3]+string[i][2]+string[i][1]+string[i][4]
    if string[i] == 'MAPOM':
        check += 1
    else:
        pass

if check > 0:
    print('yes')
else:
    print('no')