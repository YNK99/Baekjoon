def solution(s):
    
    text = []
    
    for i in s:
        if len(text) != 0 and text[-1] == i:
            text.pop()
        else:
            text.append(i)
    
    if text == []:
        return 1
    else:
        return 0