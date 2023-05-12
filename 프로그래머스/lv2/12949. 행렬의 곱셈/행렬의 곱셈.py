def solution(arr1, arr2):
    
    m, n, p = len(arr1), len(arr1[0]), len(arr2[0])
    result = []
    
    for i in range(m):
        result.append([0 for c in range(p)])
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += arr1[i][k] * arr2[k][j]
            
    return result