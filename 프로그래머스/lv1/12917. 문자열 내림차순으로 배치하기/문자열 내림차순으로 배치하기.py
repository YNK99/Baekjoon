def solution(s):
    string = []
    for i in s:
        print(i)
        string.append(i)
    string = sorted(string)[::-1]
    string = " ".join(string)
    string = string.replace(" ", "")
    answer = string
    return answer