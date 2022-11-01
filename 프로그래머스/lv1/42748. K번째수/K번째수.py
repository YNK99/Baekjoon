def solution(array, commands):
    results = []
    for i, j, k in commands:
        result = sorted(array[i-1:j])[k-1]
        results.append(result)
    return results
        
        
    