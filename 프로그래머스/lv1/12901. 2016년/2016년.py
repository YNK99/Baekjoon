import copy

def solution(a, b):
    days = 0
    weeks = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    if a == 1:
        days += b
    else:
        for i in range(1, a):
            if i == 2:
                days += 29
            elif i in month_31:
                days += 31
            else:
                days += 30   
        days += b
    return weeks[days%7]