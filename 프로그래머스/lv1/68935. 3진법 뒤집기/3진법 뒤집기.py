def solution(n):
    notation_3 = ''
    while n:
        notation_3 += str(n % 3)
        n = n // 3
    return int(notation_3, 3)
    