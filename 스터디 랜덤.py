import random
study_members = ['민구','창현','정우','혜민','성환','세영','영록']
problem_list = [list(input().split()) for _ in range(14)]
random.shuffle(study_members)
random.shuffle(problem_list)
for i in range(7):
    print(study_members[i],*problem_list[i])