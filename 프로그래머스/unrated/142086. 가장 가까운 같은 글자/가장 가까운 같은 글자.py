def solution(s):
    alpha = []
    result = []
    
    for i in s:
        if i not in alpha:
            result.append(-1)
            alpha.append(i)
        else:
            result.append(alpha[::-1].index(i) + 1)
            alpha.append(i)
    
    return result