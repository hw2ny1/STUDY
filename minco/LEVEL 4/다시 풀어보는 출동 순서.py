hero = ['B','I','A','H']
N = int(input())

for _ in range(4):
    temp = N % len(hero)
    while temp:
        n = 1
        while len(hero)-n:
            hero[n],hero[n-1] = hero[n-1],hero[n]
            n += 1 
        temp -= 1
    print(hero.pop(),end=' ')