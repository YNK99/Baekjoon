def solution(k, tangerine):
    counts = {c:0 for c in tangerine}
    
    for i in tangerine:
        counts[i] += 1
    
    counts = sorted(counts.items(), key = lambda x:-x[1])
    
    box = []
    nums = 0
    
    for count in counts:
        box.append(count[0])
        nums += count[1]
        if nums >= k:
            break
        
    result = len(box)
    return result