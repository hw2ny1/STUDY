n = int(input())
b = 0
while n >= 0:
    if n % 5 == 0:
        b += n//5
        print(b)
        break
    b += 1
    n -= 3
else:
    print(-1)