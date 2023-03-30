def solution(participant, completion):
    
    dict_participant = {c:0 for c in participant}
    
    for i in participant:
        dict_participant[i] += 1
        
    for j in completion:
        dict_participant[j] -= 1
        
    return sorted(dict_participant.items(), key = lambda x:-x[1])[0][0]