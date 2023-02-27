def backtracking(col, sum):
    global min_sum
    # 전부다 선택하였을 때, 합이 최소이면 min_sum 갱신
    if col == N:
        min_sum = min(min_sum, sum)
        return
    # 진행하는 도중 합이 min_sum을 넘으면 return
    elif sum > min_sum:
        return
    else:
        for i in range(N):
            # col열에 i행을 선택할 경우 유망한지 판단
            if promising(col, i):
                # col열에 i를 선택하고 sum에 더함
                num_list[col] = i
                backtracking(col + 1, sum+lst[i][col])
                num_list[col] = 12

def promising(col, row):
    # col열에 row를 둘려 하는 데, 존재할 경우 False
    for j in range(col):
        if row == num_list[j]:
            return False
    return True 
  
T = int(input())
for t in range(T):
    min_sum = 1e8
    N = int(input())
    num_list = [12] * N
    lst = [list(map(int, input().split())) for _ in range(N)]
    backtracking(0, 0)
    print(f'#{t+1} {min_sum}')