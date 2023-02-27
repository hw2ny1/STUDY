import sys
input = sys.stdin.readline


def check_O(temp):
    for i in range(3):
        if temp[i][0] == 'O':
            if temp[i][0] == temp[i][1] and temp[i][0] == temp[i][2]:
                return True
    for i in range(3):
        if temp[0][i] == 'O':
            if temp[0][i] == temp[1][i] and temp[0][i] == temp[2][i]:
                return True
    if temp[1][1] == 'O':
        if temp[1][1] == temp[0][0] and temp[1][1] == temp[2][2]:
            return True
        if temp[1][1] == temp[0][2] and temp[1][1] == temp[2][0]:
            return True
    return False


def check_X(temp):
    for i in range(3):
        if temp[i][0] == 'X':
            if temp[i][0] == temp[i][1] and temp[i][0] == temp[i][2]:
                return True
    for i in range(3):
        if temp[0][i] == 'X':
            if temp[0][i] == temp[1][i] and temp[0][i] == temp[2][i]:
                return True
    if temp[1][1] == 'X':
        if temp[1][1] == temp[0][0] and temp[1][1] == temp[2][2]:
            return True
        if temp[1][1] == temp[0][2] and temp[1][1] == temp[2][0]:
            return True
    return False


while True:
    temp = input().rstrip()
    if temp == 'end':
        break
    flag = 0
    tic = [list(temp[0:3]),list(temp[3:6]),list(temp[6:9])]
    if check_O(tic) and check_X(tic):
        flag = 1
    num_O = 0
    num_X = 0
    for i in range(3):
        for j in range(3):
            if tic[i][j] == 'O':
                num_O += 1
            elif tic[i][j] == 'X':
                num_X += 1
    if not num_O <= num_X <= num_O+1:
        flag = 1
    if check_O(tic) and num_O < num_X:
        flag = 1
    if check_X(tic) and num_O == num_X:
        flag = 1
    if not check_X(tic) and not check_O(tic) and num_O+num_X < 9:
        flag = 1

    if flag:
        print('invalid')
    else:
        print('valid')
