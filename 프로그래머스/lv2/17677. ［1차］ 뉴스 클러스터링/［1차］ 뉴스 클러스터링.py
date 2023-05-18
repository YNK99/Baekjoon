def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1 = [str1[c-1:c+1] for c in range(1, len(str1)) if str1[c-1:c+1].isalpha() == True]
    str2 = [str2[c-1:c+1] for c in range(1, len(str2)) if str2[c-1:c+1].isalpha() == True]
    
    s = str1 + str2
    d = []
    
    for i in str1:
        if i in str2:
            d.append(i)
            str2.remove(i)
    
    if len(s) - len(d) == 0:
        return 65536
    else:
        return int(len(d) / (len(s) - len(d)) * 65536)
