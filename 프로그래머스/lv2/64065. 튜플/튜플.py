def solution(s):
    s = s.replace("{", '').replace("}", '').split(',')
    set_s = set(s)
    s = sorted(set_s, key = lambda x:-s.count(x))
    s = [int(c) for c in s]
    return s