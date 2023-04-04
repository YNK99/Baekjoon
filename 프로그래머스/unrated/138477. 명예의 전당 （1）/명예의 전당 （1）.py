def solution(k, score):
    rank_list = []
    lows = []
    
    for i in score:
        if len(rank_list) < k:
            rank_list.append(i)
        else:
            if i > min(rank_list):
                rank_list.append(i)
                lowest = min(rank_list)
                rank_list.remove(lowest)
        lows.append(min(rank_list))
        
    return lows