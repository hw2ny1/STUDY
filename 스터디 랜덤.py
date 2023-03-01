import random
study_members = ['민구','창현','정우','혜민','성환','세영','영록']
# study_mem = ['민구','정우','성환','세영','영록']
try:
    problem_list = []
    while True:
        problem_list.append(list(input().split()))
except EOFError:
    random.shuffle(study_members)
    random.shuffle(problem_list)
    # print(*random.sample(study_mem,2))
    for i in range(7):
        print(study_members[i],*problem_list[i])
