def solution(numbers):
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    for number in number_list:
        if number in numbers:
            continue
        else:
            answer += number
    return answer