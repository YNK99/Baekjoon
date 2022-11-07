def solution(s):
    answer = ''
    last = ' '
    for i in s:
        if last == " " and i.islower() == True:
            answer += i.upper()
        elif last != " " and i.isupper() == True:
            answer += i.lower()
        else:
            answer += i
        last = i
    return answer
            
        