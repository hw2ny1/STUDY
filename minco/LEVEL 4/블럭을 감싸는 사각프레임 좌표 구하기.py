map = [list(map(int,input().split())) for i in range(4)]

def location(map):
    global block
    block = []
    for i in range(4):
        for j in range(5):
            if map[i][j] == 1:
                block.append((i,j))

def frame(map):
    location(map)
    frame_min = [111,111]
    for i,j in block:
        frame_min[0] = min(i,frame_min[0])
        frame_min[1] = min(j,frame_min[1])
    print(f'({frame_min[0]},{frame_min[1]})')

    frame_max = [-111,-111]
    for i,j in block:
        frame_max[0] = max(i,frame_max[0])
        frame_max[1] = max(j,frame_max[1])
    print(f'({frame_max[0]},{frame_max[1]})')

frame(map)