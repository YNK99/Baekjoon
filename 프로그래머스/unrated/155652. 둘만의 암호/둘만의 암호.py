def solution(s, skip, index):
    answer = ''
    skip = [c for c in skip]
    skip_alphabets  =   [chr(c) for c in range(97, 123) if chr(c) not in skip]
    
    for i in s:
        idx = skip_alphabets.index(i) + index
        answer += skip_alphabets[idx%len(skip_alphabets)]
        
    return answer