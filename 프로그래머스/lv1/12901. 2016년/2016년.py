import copy

def solution(a, b):
    answer = ''
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    days = 0
    for i in range(1, a):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            days += 31
        elif i == 2:
            days += 29
        else:
            days += 30
    days += b
    answer = (week[(days % 7) - 1])
    return answer