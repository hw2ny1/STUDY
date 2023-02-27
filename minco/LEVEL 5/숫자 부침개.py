num = int(input())
n = int(input())

for _ in range(n):
    num = int(num)*2
    num = str(num)[::-1]

print(num)