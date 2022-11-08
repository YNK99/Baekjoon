def solution(s):
    my_list = ''
    
    for i in s:
        my_list += i
        if my_list[-2:] == '()':
            my_list = my_list[:-2]
            
    if my_list == '':
        answer = True
    else:
        answer = False
        
    return answer