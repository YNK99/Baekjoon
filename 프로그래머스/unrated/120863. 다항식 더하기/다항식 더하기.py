def solution(polynomial):
    polynomial = polynomial.split('+')
    x_num = 0
    num = 0
    polynomial = [c.strip() for c in polynomial]
    for i in polynomial:
        if i[-1] == 'x':
            if i[:-1] == '':
                x_num += 1
            else:
                x_num += int(i[:-1])
        else:
            num += int(i)
    if x_num == 0:
        return str(num)
    elif num == 0:
        if x_num == 1:
            return 'x'
        else:
            return str(x_num) + 'x'
    elif x_num == 0 and num == 0:
        return str(0)
    else:
        if x_num == 1:
            return 'x + ' + str(num)
        else:
            return str(x_num) + 'x + ' + str(num)