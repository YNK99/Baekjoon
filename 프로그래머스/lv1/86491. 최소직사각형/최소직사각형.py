def solution(sizes):
    answer = 0
    g = []
    s = []
    
    for size in sizes:
        if size[0] <= size[1]:
            g.append(size[1])
            s.append(size[0])
        else:
            g.append(size[0])
            s.append(size[1])
    answer = max(g) * max(s)
    return answer