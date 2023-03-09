def solution(food):
    result = ''
    for i, j in enumerate(food):
        num = str(i) * (j // 2)
        result = result + num
    
    return result + '0' + result[::-1]