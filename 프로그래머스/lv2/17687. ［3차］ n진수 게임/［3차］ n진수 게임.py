def solution(n, t, m, p):
    
    def f(number, base):
        result = ""

        while number != 0:
            number, mod = divmod(number, base)

            if base > 10 and (10 <= mod <= 15):
                result += "ABCDEF"[mod % 10]
            else:
                result += str(mod)

        return result[::-1]
    
    result = '0'
    
    for i in range(t * m + 1):
        result += f(i, n)

    return result[p-1::m][:t]