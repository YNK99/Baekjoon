def solution(survey, choices):
    answer = ''
    
    types = ["R", "T", "C", "F", "J", "M", "A", "N"]
    result = {c:0 for c in types}

    for i, j in zip(survey, choices):
        if j < 4:
            result[i[0]] += (j-4) * -1
        else:
            result[i[1]] += (j-4)

    for k in range(0, 8, 2):
        type1, type2 = types[k:k+2][0], types[k:k+2][1]
        if result[type1] > result[type2]:
            answer += type1
        elif result[type1] < result[type2]:
            answer += type2
        else:
            answer += min(type1, type2)
    
    return answer