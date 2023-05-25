def solution(record):
    
    user = {c.split()[1]:c.split()[2] for c in record if len(c.split()) == 3}
    result = []

    for i in record:
        if i[0] == 'E': 
            result.append('{}님이 들어왔습니다.'.format(user[i.split()[1]]))
        if i[0] == 'L':
            result.append('{}님이 나갔습니다.'.format(user[i.split()[1]]))
                    
    return result
