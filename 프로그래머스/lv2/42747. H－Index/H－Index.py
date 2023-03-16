def solution(citations):
    citations = sorted(citations)
    length = len(citations)
    
    for i in range(length):
        if citations[i] >= length - i:
            return length - i
    return 0