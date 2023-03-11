def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for i in babbling:    
        for word in words:
            if word + word not in i:
                i = i.replace(word, " ")

        i = i.replace(" ", "")
        if i == "":
            cnt += 1
            
    return cnt
        