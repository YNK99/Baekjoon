def solution(dartResult):
    
    dartResult = dartResult.replace('S', ' S ')
    dartResult = dartResult.replace('D', ' D ')
    dartResult = dartResult.replace('T', ' T ')
    dartResult = dartResult.replace('*', ' * ')
    dartResult = dartResult.replace('#', ' # ')
    dartResult = dartResult.split()
    
    scores = [str(c) for c in range(0, 11)]
    answer = []
    
    for dart in dartResult:
        if dart in scores:
            answer.append(int(dart))
            
        if dart == 'S':
            answer[-1] = answer[-1] ** 1
        if dart == 'D':
            answer[-1] = answer[-1] ** 2
            
        if dart == 'T':
            answer[-1] = answer[-1] ** 3
            
        if dart == '*':
            if len(answer) == 1:
                answer[0] = answer[0] * 2
            else:
                answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * 2
                
        if dart == '#':
            answer[-1] = answer[-1] * -1
            
        else:
            continue
            
    return sum(answer)