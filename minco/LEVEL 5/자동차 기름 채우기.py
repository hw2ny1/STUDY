binary = list(str(input()))

def binary_serch(binary):
    left = 0
    right = len(binary)-1
    mid = (left + right)//2
    while left < right:
        mid = (left + right)//2
        if binary[mid] == '#' and binary[mid+1] == '_':
            return mid + 1
        elif binary[mid] == '#':
            left = mid + 1
        else:
            right = mid - 1
    return None

print(f'{binary_serch(binary)*10}%')
