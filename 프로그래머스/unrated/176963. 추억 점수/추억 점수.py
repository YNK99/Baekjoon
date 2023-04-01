def solution(name, yearning, photo):
    my_dict = {c[0]:c[1] for c in zip(name, yearning)}
    result = []
    
    for i in photo:
        y = 0
        for j in i:
            if j in name:
                y += my_dict[j]
            else:
                pass
        result.append(y)
        
    return result