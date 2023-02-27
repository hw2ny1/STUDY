n = int(input())

def sqrt(x):
    if x < 2:
        return x
    left = 0
    right = x//2
    result = 0
    while left <= right:
        mid = (left + right)//2
        temp = mid*mid
        if temp == x:
            return mid
        elif temp < x:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    return result

print(sqrt(n))