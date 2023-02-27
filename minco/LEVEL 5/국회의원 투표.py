n, m = map(int,input().split())
num_people = list()
vote = list()
max_vote = 0

for _ in range(m):
    a, b = input().split()
    num_people.append((a,b))
    vote.append(a)

for i in range(n):
    max_vote = max(max_vote,vote.count(str(i)))
    if vote.count(str(i)) >= max_vote:
        temp = i

for i in range(m):
    if num_people[i][0] == str(temp):
        print(num_people[i][1],end = ' ')