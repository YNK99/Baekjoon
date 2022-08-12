def solution(lottos, win_nums):
    max_num = 7
    min_num = 7
    for lotto in lottos:
        for num in win_nums:
            if lotto == 0:
                max_num -= 1
                break
            else:
                if lotto == num:
                    max_num -= 1
                    min_num -= 1
                    break
                else:
                    continue
    if max_num > 6:
        max_num = 6
    
    if min_num > 6:
        min_num = 6
        
    answer = [max_num, min_num]
    return answer