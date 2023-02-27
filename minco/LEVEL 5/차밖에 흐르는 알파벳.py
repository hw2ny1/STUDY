word = list(map(ord,list(input())))
N = len(word)

while word.count(95) != N:
    for i in range(N):
        print(chr(word[i]),end='')
    print('')
    for i in range(N):
        if word[i] >= 65 and word[i] <= 90:
            word[i] -= 1
        if word[i] < 65:
            word[i] = 95

for i in range(N):
        print(chr(word[i]),end='')