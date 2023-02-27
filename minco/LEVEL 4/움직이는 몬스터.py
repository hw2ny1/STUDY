map = [list(str(input())) for _ in range(4)]

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def location(map):
    global monster
    monster = []
    for j in alph:
        for i in range(4):
            if map[i].count(j)>0:
                monster.append((i,map[i].index(j)))

def movement(map):
    location(map)
    #오른쪽
    for x,y in monster:
        if y != 2 and map[x][y+1] == '_':
            map[x][y],map[x][y+1] = map[x][y+1],map[x][y]

    location(map)
    #아래
    for x,y in monster:
        if x != 4 and map[x+1][y] == '_':
            map[x+1][y],map[x][y] = map[x][y],map[x+1][y]
    
    location(map)
    #왼쪽
    for x,y in monster:
        if y != 0 and map[x][y-1] == '_':
            map[x][y],map[x][y-1] = map[x][y-1],map[x][y]

    location(map)
    #위쪽
    for x,y in monster:
        if x != 0 and map[x-1][y] == '_':
            map[x-1][y],map[x][y] = map[x][y],map[x-1][y]

    location(map)
    #오른쪽
    for x,y in monster:
        if y != 2 and map[x][y+1] == '_':
            map[x][y],map[x][y+1] = map[x][y+1],map[x][y]

movement(map)
#맵 출력
location(map)
for i in range(4):
    for j in range(3):
        print(map[i][j],end = '')
    print('')


