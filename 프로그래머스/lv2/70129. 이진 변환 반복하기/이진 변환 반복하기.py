def solution(s):
    cnt = 0
    zero_count = 0
    while s != "1":
        zero_count += s.count("0")
        s = len(s.replace("0", ""))
        s = format(s, 'b')
        cnt += 1
    return [cnt, zero_count]