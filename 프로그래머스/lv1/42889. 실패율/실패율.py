def solution(N, stages):
    counter = {c:0 for c in range(1, N+1)}
    people = len(stages)
    
    for i in stages:
        if i > N:
            pass
        else:
            counter[i] += 1
    
    fail = {}
    
    for c in counter.items():
        if people == 0:
            fail[c[0]] = 0
        else:
            fail[c[0]] = c[1] / people
            people -= c[1]

    return [c[0] for c in sorted(fail.items(), key = lambda x:-x[1])]
    