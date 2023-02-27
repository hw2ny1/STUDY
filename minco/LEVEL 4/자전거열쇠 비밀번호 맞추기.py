#ord chr 65 91

def bikekey(anser):
    count = 1
    start = [65 for _ in range(4)]
    while anser != start:
        for i in range(3):
            if start[3-i] == 91:
                start[3-i] = 65
                start[2-i] += 1
        count += 1
        start[3] += 1
    print(count)

N = int(input())
for _ in range(N):
    anser = list(map(ord,list(input())))
    bikekey(anser)