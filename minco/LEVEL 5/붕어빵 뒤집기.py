arr = [['A','B','C','E','F','G'],
       ['H','I','J','K','L','M'],
       ['N','O','P','Q','R','S']]

back = [['#' for _ in range(6)] for _ in range(3)]

words = list(str(input()))

for k in words:
    for i in range(3):
        for j in range(6):
            if arr[i][j] == k:
                arr[i][j],back[i][j] = back[i][j],arr[i][j]
                if i <= 1:
                    arr[i+1][j],back[i+1][j] = back[i+1][j],arr[i+1][j]
                if i >= 1:
                    arr[i-1][j],back[i-1][j] = back[i-1][j],arr[i-1][j]
                if j < 5:
                    arr[i][j+1],back[i][j+1] = back[i][j+1],arr[i][j+1]
                if j > 0:
                    arr[i][j-1],back[i][j-1] = back[i][j-1],arr[i][j-1]

for i in range(3):
    for j in range(6):
        print(arr[i][j],end='')
    print('')