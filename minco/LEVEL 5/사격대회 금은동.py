n = int(input())
player = list()
for i in range(n):
    a,b = map(str,input().split())
    player.append((a,int(b),i))
    player.sort(key=lambda x: (x[1],x[2]),reverse=True)
    for j in range(3):
        try:
            print(player[j][0],end = ' ')
        except:
            pass
    print('')