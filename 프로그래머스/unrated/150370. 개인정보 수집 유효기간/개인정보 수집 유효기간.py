def solution(today, terms, privacies):
    result = []
    
    today = today.split(".")
    today = (int(today[0])-2000)*12*28 + (int(today[1])-1)*28 + int(today[2])
    term_list = {c.split(" ")[0]:int(c.split(" ")[1]) for c in terms}
    
    for cnt, privacy in enumerate(privacies):
        privacy, term = privacy.split(" ")
        time = privacy.split(".")
        year, month, day = int(time[0]), int(time[1]), int(time[2])
        during = (year - 2000)*12*28 + (month-1)*28 + int(day)
        if today - during > term_list[term] * 28 - 1:
            result.append(cnt+1)
        
    return result