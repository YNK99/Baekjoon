def solution(X, Y):
    X, Y = list(X), list(Y)
    result = ''
    
    for i in range(0, 10):
        i = str(i)
        x, y = X.count(i), Y.count(i)
        c = min(x, y)
        result += i * c
    
    if result == '':
        return "-1"
    else:
        result = sorted(result)[::-1]
        if result[0] == "0":
            return "0"
        else:
            return "".join(result)