import random
study_members = ['민구','창현','정우','정희','성환','세영','혜민','영록']
bad_guys = []
try:
    problem_list = []
    while True:
        problem_list.append(list(input().split()))
except EOFError:
    for bad in bad_guys:
        study_members.remove(bad)
    for _ in range(len(bad_guys)):
        study_members.extend(random.sample(study_members, 1))
    random.shuffle(study_members)
    random.shuffle(problem_list)
    for i in range(len(study_members)):
        print(study_members[i],*problem_list[i])
