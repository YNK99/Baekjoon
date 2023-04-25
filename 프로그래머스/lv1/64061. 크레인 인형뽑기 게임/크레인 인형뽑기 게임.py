def solution(board, moves):
    basket = []
    
    for move in moves:
        for b in board:
            if b[move-1] != 0:
                basket.append(b[move-1])
                b[move-1] = 0
                break
                
    basket_pop = []
    cnt = 0
    
    for i in basket:
        basket_pop.append(i)
        if len(basket_pop) >= 2:
            if basket_pop[-1] == basket_pop[-2]:
                basket_pop.pop()
                basket_pop.pop()
                cnt += 2
                
    return cnt