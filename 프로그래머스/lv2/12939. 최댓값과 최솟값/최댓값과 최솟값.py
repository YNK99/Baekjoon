def solution(s):
    max_value = max(map(int, s.split(" ")))
    min_value = min(map(int, s.split(" ")))
    return "{} {}".format(min_value, max_value)