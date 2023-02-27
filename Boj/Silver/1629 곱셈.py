def devide_pow(A,B):
    if B == 1:
        return A%C
    else:
        x = devide_pow(A,B//2)
        if B % 2:
            return x*x*A%C
        else:
            return x*x%C


A, B, C = map(int, input().split())
print(devide_pow(A,B))