def solution(n):
    one_count = format(n, "b").count("1")
    num = n + 1
    
    while format(num, "b").count("1") != one_count:
        num += 1
        
    return num