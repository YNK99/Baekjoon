def solution(answers):
    score_dict = {str(c):0 for c in range(1, 4)}
    patten1, patten2, patten3 = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        answer1, answer2, answer3, answer = patten1[i % 5], patten2[i % 8], patten3[i % 10], answers[i]
        if answer1 == answer:
            score_dict['1'] += 1
        if answer2 == answer:
            score_dict['2'] += 1
        if answer3 == answer:
            score_dict['3'] += 1
            
    max_score = max(score_dict.values())
    return [int(c[0]) for c in score_dict.items() if c[1] == max_score]