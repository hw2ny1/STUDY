def solution(jobs):
    jobs = sorted(jobs, key=lambda x:(x[0],x[1]))
    j = jobs.pop(0)
    fin = j[0]+j[1]
    wait = []
    comp = [j[1]]
    while jobs:
        wait = []
        for j in jobs:
            if j[0] <= fin:
                wait.append(j) 
        if wait:
            wait.sort(key=lambda x: x[1])
            comp.append(fin-wait[0][0]+wait[0][1])
            fin += wait[0][1]
            jobs.remove(wait[0])
        else:
            j = jobs.pop(0)
            comp.append(j[1])
            fin = j[0]+j[1]
    return sum(comp) // len(comp)