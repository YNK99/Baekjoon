def solution(n, words):
    last_words = []
    
    for cnt, word in enumerate(words):
        if cnt == 0:
            last_words.append(word)
        else:
            if word in last_words or last_words[-1][-1] != word[0]:
                break
            else:
                last_words.append(word)
        
    if words == last_words:
        return [0, 0]
    else:
        return [cnt % n + 1, cnt // n + 1]