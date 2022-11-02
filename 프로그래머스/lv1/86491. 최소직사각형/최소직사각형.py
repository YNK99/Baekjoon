def solution(sizes):
    w = []
    h = []
    for i, j in sizes:
        if i < j:
            h.append(i)
            w.append(j)
        else:
            h.append(j)
            w.append(i)
    answer = max(w) * max(h)
    return answer