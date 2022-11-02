def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i):
            answer.append(numbers[i] + numbers[j])
    answer = sorted(set(answer))
    return answer