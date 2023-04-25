import random
study_members = [('정희',21),('성환',1),('세영',2),('민구',12),('영록',1)]
# bad_guys = [('창현',1)]
problem_num = 6
study_member = []
total_n = 0

for i, n in study_members:
    total_n += n
    for _ in range(n):
        study_member.append(i)

try:
    problem_list = []
    while True:
        problem_list.append(list(input().split()))
except EOFError:
    # for bad in bad_guys:
    #     study_members.remove(bad)
    # for _ in range(len(bad_guys)):
    #     study_members.extend(random.sample(study_members, 1))
    random.shuffle(problem_list)
    cost = [random.randint(1, problem_num * 2) for i in range(problem_num)]
    for i in range(problem_num):
        print(study_member[random.randint(0,total_n-1)],*problem_list[i],f'가중치 {cost[i]}')