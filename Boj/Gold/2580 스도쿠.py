def promising_x(x, num):
    for i in range(9):
        if sudoku[x][i] == num:
            return False
    return True

def promising_y(y, num):
    for i in range(9):
        if sudoku[i][y] == num:
            return False
    return True

def promising_z(x,y,num):
    for i in range(3):
        for j in range(3):
            if sudoku[(x//3)*3+i][(y//3)*3+j] == num:
                return False
    return True

def backtracking(cnt):
    if cnt == end:
        for sudo in sudoku:
            print(*sudo)
        exit(0)
    else:
        x, y = stack[cnt]
        for i in range(1, 10):
            if promising_x(x, i) and promising_y(y, i) and promising_z(x, y, i):
                sudoku[x][y] = i
                backtracking(cnt+1)
                sudoku[x][y] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]
stack = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            stack.append([i, j])

end = len(stack)
backtracking(0)
