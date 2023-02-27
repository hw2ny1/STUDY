N = int(input())
result = ''

def soccer(N,result):
    if len(result) == N:
        print(result)
        return
    if len(result) < N:
        for i in range(2):
            if i == 0:
                result += 'o'
                soccer(N,result)
                result = result[:-1]
            else:
                result += 'x'
                soccer(N,result)
                
soccer(N,result)