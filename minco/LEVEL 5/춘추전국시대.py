N = int(input())
country = [i for i in range(N)]
people = list(map(int,input().split()))

def alph(x):
    temp = 'ABCDEFGHIJKL'
    return int(temp.find(x))

def union(situation,a,b):
    global country
    a, b = alph(a), alph(b)
    if a > b:
        a,b = b,a
    if situation == 'alliance':
        country[b] = a
    elif situation == 'war':
        war(a,b)

def war(a,b):
    global country,people
    temp_a,temp_b = 0,0
    temp_a_list,temp_b_list = [],[]
    for i in range(N):
        if country[i] == country[a]:
            temp_a += people[i]
            temp_a_list.append(i)
        if country[i] == country[b]:
            temp_b += people[i]
            temp_b_list.append(i)
    if temp_a > temp_b:
        for i in temp_b_list:
            coutnry[i] = 'x'
    else:
        for i in temp_a_list:
            country[i] = 'x'

S = int(input())
for _ in range(S):
    s,a,b = input().split()
    union(s,a,b)

while country.count('x') > 0:
    country.remove('x')

print(len(country))