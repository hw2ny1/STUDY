import sys
input = sys.stdin.readline

def palindrom(string):
    str = list(string);i = 0;j = len(str)-1;flag = 0
    while i < j:
        if str[i] == str[j]:i += 1;j -= 1
        elif str[i+1] == str[j] and str[i] == str[j-1]:
            if palindrom(string[i+1:j+1]) >= palindrom(string[i:j]):flag += 1;j -= 1
            else:i += 1;flag += 1
        elif str[i+1] == str[j]:i += 2;j -= 1;flag += 1
        elif str[i] == str[j-1]:j -= 2;i += 1;flag += 1
        else:return 2
    if flag == 1:return 1
    elif flag == 0:return 0
    else:return 2


N = int(input())
for _ in range(N):
    print(palindrom(input().strip()))