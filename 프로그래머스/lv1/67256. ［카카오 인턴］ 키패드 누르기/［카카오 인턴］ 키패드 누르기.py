def solution(numbers, hand):
    
    pad = [[1, 4, 7, 10], [2, 5, 8, 0], [3, 6, 9, 12]]
    left_hand, right_hand = [0, 3], [2, 3]
    
    result = ''
    
    for num in numbers:
        if num in pad[0]:
            left_hand = [0, pad[0].index(num)]
            # print(num, left_hand, 'left')
            result += 'L'
        elif num in pad[2]:
            right_hand = [2, pad[2].index(num)]
            # print(num, right_hand, 'right')
            result += 'R'
        else:
            for c, p in enumerate(pad):
                if num in p:
                    # print(num, c, p.index(num))
                    
                    right_dis = abs(right_hand[0] - c) + abs(right_hand[1] - p.index(num))
                    left_dis = abs(left_hand[0] - c) + abs(left_hand[1] - p.index(num))
                    
                    # print(num, right_dis, right_hand, 'right_hand')
                    # print(num, left_dis, left_hand, 'left_hand')
                    
                    if left_dis < right_dis:
                        # print('left')
                        result += 'L'
                        left_hand = [c, p.index(num)]
                    elif left_dis > right_dis:
                        # print('right')
                        result += 'R'
                        right_hand = [c, p.index(num)]
                    else:
                        if hand == 'right':
                            # print('right')
                            result += 'R'
                            right_hand = [c, p.index(num)]
                        else:
                            # print('left')
                            result += 'L'
                            left_hand = [c, p.index(num)]
    return result