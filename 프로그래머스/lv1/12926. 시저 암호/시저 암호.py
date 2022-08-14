def solution(s, n):
    answer = ''
    small_alphabet = [chr(i) for i in range(97, 123)]
    big_alphabet = [chr(j) for j in range(65, 91)]
    for k in s:
        if k in small_alphabet:
            if small_alphabet.index(k) + n > 25:
                answer += small_alphabet[small_alphabet.index(k) + n - 25 - 1]
            else:
                answer += small_alphabet[small_alphabet.index(k) + n]
        elif k == " ":
            answer += " "
        else:
            if big_alphabet.index(k) + n > 25:
                answer += big_alphabet[big_alphabet.index(k) + n - 25 - 1]
            else:
                answer += big_alphabet[big_alphabet.index(k) + n]
    return answer