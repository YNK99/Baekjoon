def solution(cards1, cards2, goal):
        
    for i in goal:
        if len(cards1) > 0 and i == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and i == cards2[0]:
            cards2.pop(0) 
        else:
            return "No"
    return "Yes"
            
    
    
    
    
    
    
    
    
    
    while True:
        print(goal)
        print('card1', cards1)
        print('cards2', cards2)
        if goal == []:
            return "Yes"
        else:
            if goal[0] == cards1[0] and last != 'cards1':
                goal.pop(0)
                cards1.pop(0)
                last = 'cards1'
            elif goal[0] == cards2[0] and last != 'cards2':
                goal.pop(0)
                cards2.pop(0)
                last = 'cards2'
            else:
                print('No')
                break