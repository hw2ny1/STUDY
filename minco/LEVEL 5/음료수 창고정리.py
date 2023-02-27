bottle = [list(str(input())) for _ in range(5)]
todo = list(map(int,input().split()))

for i in todo:
    bottle[i].sort()


for i in range(5):
    print(bottle[i][0],end=' ')