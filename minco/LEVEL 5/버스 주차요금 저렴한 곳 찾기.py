fee = [1,2,3,3,5,1,0,1,3]

min_fee = 10
n = int(input())
for i in range(10-n):
    temp = 0
    for j in range(n):
        temp += fee[i+j]
    min_fee = min(temp,min_fee)
    

print(min_fee)