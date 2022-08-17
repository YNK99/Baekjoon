def solution(array, commands):
    array = [array] * len(commands)
    answer = []
    for a, command in zip(array, commands):
        new = sorted(a[command[0]-1 : command[1]])
        f = new[command[2] - 1]
        answer.append(f)
    return answer