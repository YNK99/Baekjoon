def solution(s):
    
    right = ['()', '[]', '{}']
    x = len(s)
    cnt = 0
    
    for i in range(x):
        is_right = s
        while '()' in is_right or '[]' in is_right or '{}' in is_right:
            for j in right:
                is_right = is_right.replace(j, '')
        if is_right == '':
            cnt += 1
        s = s[1:] + s[0]
    
    return cnt