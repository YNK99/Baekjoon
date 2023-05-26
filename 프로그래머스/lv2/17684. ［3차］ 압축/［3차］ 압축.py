def solution(msg):
    number = [chr(c) for c in range(65, 91)]    
    msg = list(msg)    
    last = ''
    answer = []
    
    for m in msg:
        last += m
        if last not in number:
            answer.append(number.index(last[:-1]) + 1)
            number.append(last)
            last = last[-1:]
    
    answer.append(number.index(last) + 1)
    
    return answer