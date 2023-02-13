def solution(s):
    str_list = ['', 0, 0]
    answer = 0
    
    for i in s:
        if str_list[0] == '':
            str_list[0] = i
            str_list[1] += 1
        else:
            if str_list[0] == i:
                str_list[1] += 1
            else:
                str_list[2] += 1
            if str_list[1] == str_list[2]:
                answer += 1
                str_list = ['', 0, 0]
    if str_list != ['', 0, 0]:
        answer += 1
    
    return answer