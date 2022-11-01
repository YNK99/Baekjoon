from collections import deque

def solution(s, n):
    answer = ''
    small = [chr(i) for i in range(97, 123)]
    big = [chr(j) for j in range(65, 91)]
    rotation_small = small[n:] + small[0:n]
    rotation_big = big[n:] + big[0:n]
    answer = ''
    for i in s:
        if i in small:
            answer += rotation_small[small.index(i)]
        elif i in big:
            answer += rotation_big[big.index(i)]
        else:
            answer += ' '
    return answer